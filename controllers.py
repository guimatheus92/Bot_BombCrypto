import requests
import json
import asyncio
import datetime
import logging
import pyautogui
import os
import pathlib
import datetime
import time
import yaml
import telegram

def read_configurations():
    '''
    Function to read the configuration from .yaml file
    '''

    with open(os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), "config.yaml"), 'r', encoding='utf8') as s:
        stream = s.read()
    return yaml.safe_load(stream)

try:
    streamConfig = read_configurations()
    telegram_integration = streamConfig['telegram_options']['telegram_integration']
    telegram_token = streamConfig['telegram_options']['telegram_token']    
    telegram_chatid = streamConfig['telegram_options']['telegram_chatid']        
    create_logfiles = streamConfig['bot_options']['create_logfiles']
    delete_old_logfiles = streamConfig['bot_options']['delete_old_logfiles']
    delete_old_folders = streamConfig['bot_options']['delete_old_folders']
except FileNotFoundError:
    print('Error: config.yaml file not found, make sure config.yaml are placed in the folder..')
    exit()

async def delete_folders():
    '''
    Function do delete old folders created from this bot
    '''

    if delete_old_folders != False:
        # Path to log folder
        rootdir = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve())
        # Today's date
        todays_date = datetime.date.today()

        for folder in os.walk(rootdir):
            folder_name = pathlib.Path(folder[0]).name    
            try:
                if datetime.datetime.strptime(folder_name, '%Y-%m-%d').date() != todays_date:
                    os.rmdir(str(os.path.join(folder[0])))
                    print('%s folder deleted!\n' % folder_name)
                    pass
            except Exception as e:
                #print("Exception: " + str(e))
                pass    

async def delete_log_files():
    '''
    Function do delete old log files from the log folder.
    '''

    if delete_old_logfiles != False:
        # Path to log folder
        filesPath = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'logs')
        # Today's date
        todays_date = datetime.date.today()

        # For file in folder
        for file in pathlib.Path(filesPath).glob('*'):
            if file.is_file():
                # If file has the extension .log
                if file.suffix == '.log':
                    file_dt = datetime.datetime.strptime(file.stem, '%Y-%m-%d').date()
                    # If file is different from today's date
                    if file_dt != todays_date:
                        os.remove(str(file.absolute()))
                        print('Log file %s deleted from folder!\n' % file.stem)
                        pass

def start_telegram():
    '''
    Function to start telegram
    '''

    if telegram_integration != False:        
        #print('Initializing Telegram...')
        TelegramBot = telegram.Bot(token=telegram_token)
        return TelegramBot
    else:
        print('Telegram integration not enabled on config.yaml file...')

def get_telegram_chat_id():
    '''
    Function to get telegram chat id from telegram token
    It's not possible to retrieve chat id, if telegram token is None
    '''
    
    if telegram_chatid is None:
        url = 'https://api.telegram.org/bot' + str(telegram_token) + '/getUpdates'    
        response = requests.request("GET", url)
        telegram_response = json.loads(response.text)
        chat_id = telegram_response['result'][0]['message']['chat']['id']
        return chat_id

def send_telegram_msg(message):
    '''
    Function to send Telegram message
    '''

    if telegram_chatid is None:
        chat_id = get_telegram_chat_id()
    else:
        chat_id = telegram_chatid

    TelegramBot = start_telegram()    
    TelegramBot.send_message(text=message, chat_id=chat_id)

# Function to send Telegram pictures
def SendTelegramPic():
    print(True)
        
def take_screenshot(folder='', sub_folder='', info = ''):
    '''
    Function to take a screenshot and save the file wherever you want.
    '''

    if folder != '':
        path = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', folder)
    else:
        path = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img')
    if not os.path.exists(path):
        os.mkdir(path)
    if sub_folder != '':
        path = os.path.join(path,sub_folder)
        if not os.path.exists(path):
            os.mkdir(path)

    path = os.path.join(path, time.strftime("%Y-%m-%d"))
    if not os.path.exists(path):
        os.mkdir(path)            
    if info != '':
        info = f"_{info}"

    # File name        
    file = time.strftime(f"%Y-%m-%d-%H-%M-%S{info}.jpg")
    # Take screenshot
    myScreenshot = pyautogui.screenshot()
    # Save screenshot
    myScreenshot.save(os.path.join(path, file))

async def initialize_pyautogui():
    '''
    Function to initialize pyautogui library.
    Reference: https://pyautogui.readthedocs.io/en/latest/quickstart.html
    '''

    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 1

def run_once(f):
    '''
    Decorator function to run a function only once
    '''
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

# Define the logging level and the file name
async def setup_logger(telegram_integration=False):
    '''
    Function to log the steps you need.
    You can define the logging level and the file name.
    To setup as many loggers as you want.
    '''  

    filename = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'logs', str(datetime.date.today()) + '.log')
    formatter = logging.Formatter('%(levelname)s | Function: %(funcName)s | %(asctime)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    level = logging.INFO

    if create_logfiles != False:
        handler = logging.FileHandler(filename, 'a')    
        handler.setFormatter(formatter)

    consolehandler = logging.StreamHandler()
    consolehandler.setFormatter(formatter)
 
    class TelegramHandler(logging.Handler):

        def emit(self, record):
            message = self.format(record)
            send_telegram_msg(message)
            # send_telegram_msg(message, record.levelno)    # Passing level
            # send_telegram_msg(message, record.levelname)  # Passing level name

    logger = logging.getLogger('logs')
    if logger.hasHandlers():
        # Logger is already configured, remove all handlers
        logger.handlers = []
    else:
        logger.setLevel(level)
        if create_logfiles != False:
            logger.addHandler(handler)
        logger.addHandler(consolehandler)        
        if telegram_integration != False:
            telegram_handler = TelegramHandler()
            logger.addHandler(telegram_handler)        

    return logger

async def countdown_timer():
    '''
    Function to countdown time before start
    '''

    # Countdown timer    
    print("Starting Bot", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        time.sleep(1)
    print(" Bot started!\n")