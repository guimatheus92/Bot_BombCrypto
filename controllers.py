import sys
import requests
import json
import datetime
import logging
import pyautogui
import os
import pathlib
import datetime
import time
import yaml
import telegram
import pandas as pd
from pywinauto import Desktop

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
    telegram_pic_integration = streamConfig['telegram_options']['telegram_pic_integration']
    telegram_token = streamConfig['telegram_options']['telegram_token']    
    telegram_chatid = streamConfig['telegram_options']['telegram_chatid']        
    create_logfiles = streamConfig['bot_options']['create_logfiles']
    delete_old_logfiles = streamConfig['bot_options']['delete_old_logfiles']
    delete_old_folders = streamConfig['bot_options']['delete_old_folders']
    multiaccount_names = streamConfig['bot_options']['multiaccount_names']
    enable_multiaccount = streamConfig['bot_options']['enable_multiaccount']
    create_bat = streamConfig['bot_options']['create_bat_file']
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
        if telegram_token is None:
            print('Telegram token not found on config.yaml file...')
        else:
            TelegramBot = telegram.Bot(token=telegram_token)
        return TelegramBot
    else:
        print('Telegram integration not enabled on config.yaml file...')

def get_telegram_chat_id():
    '''
    Function to get telegram chat id from telegram token
    It's not possible to retrieve chat id, if telegram token is None
    '''
    
    try:
        if telegram_chatid is None:
            if telegram_token is None:
                print('Telegram token not found on config.yaml file...')
            else:
                url = 'https://api.telegram.org/bot' + str(telegram_token) + '/getUpdates'
                response = requests.request("GET", url)
                telegram_response = json.loads(response.text)
                chat_id = telegram_response['result'][0]['message']['chat']['id']
            return chat_id
    except:
        print('Telegram chat id not found! Make sure to send at least any message to your bot on Telegram, so the endpoint from API might work corectly! Exiting bot..')
        os._exit(0)

def send_telegram_msg(message, bot_name=''):
    '''
    Function to send Telegram message
    '''
    if telegram_integration != False:
        if telegram_chatid is None:
            chat_id = get_telegram_chat_id()
        else:
            chat_id = telegram_chatid
                
        if bot_name != '':
            TelegramBot = start_telegram()
            TelegramBot.send_message(text='Bot (' + str(bot_name) + '): ' + message, chat_id=chat_id)
        else:
            pass

# Function to send Telegram pictures
def send_telegram_pic(image):
    '''
    Function to send Telegram pictures
    '''
    if telegram_pic_integration != False:
        if telegram_chatid is None:
            chat_id = get_telegram_chat_id()
        else:
            chat_id = telegram_chatid
                
        try:
            TelegramBot = start_telegram()
            TelegramBot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))
        except:
            pass
        
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
    path_file = os.path.join(path, file)
    try:
        # Save screenshot
        pyautogui.screenshot(path_file)
    except:
        pass
    return path_file

async def initialize_pyautogui():
    '''
    Function to initialize pyautogui library.
    Reference: https://pyautogui.readthedocs.io/en/latest/quickstart.html
    '''

    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 1

# Define the logging level and the file name
def setup_logger(telegram_integration=False, bot_name=''):
    '''
    Function to log the steps you need.
    You can define the logging level and the file name.
    To setup as many loggers as you want.
    '''
    
    if not os.path.exists(os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'logs')):
        os.mkdir(os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'logs'))
    filename = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'logs', str(datetime.date.today()) + '.log')
    if bot_name != '':
        formatter = logging.Formatter('%(levelname)s | Function: %(funcName)s | %(asctime)s: Bot (' + str(bot_name) + '):  %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    else:
        formatter = logging.Formatter('%(levelname)s | Function: %(funcName)s | %(asctime)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    
    level = logging.INFO

    if create_logfiles != False:
        handler = logging.FileHandler(filename, 'a')
        handler.setFormatter(formatter)

    consolehandler = logging.StreamHandler(sys.stdout)
    consolehandler.setFormatter(formatter)
 
    if telegram_integration != False and telegram_token is not None:
        class TelegramHandler(logging.Handler):

            def emit(self, record):
                message = self.format(record)
                try:
                    send_telegram_msg(message, bot_name)
                    # send_telegram_msg(message, record.levelno)    # Passing level
                    # send_telegram_msg(message, record.levelname)  # Passing level name
                except:
                    pass

    logger = logging.getLogger('logs')
    if logger.hasHandlers():
        # Logger is already configured, remove all handlers
        logger.handlers = []
    
    logger.setLevel(level)
    if create_logfiles != False:
        logger.addHandler(handler)
    logger.addHandler(consolehandler)        
    if telegram_integration != False and telegram_token is not None:
        telegram_handler = TelegramHandler()
        logger.addHandler(telegram_handler)        

    return logger

def get_browser():

    logger = setup_logger(telegram_integration=True)

    # Get all profiles from Brave web browser
    profiles = multiaccount_names
    if enable_multiaccount != False:
        logger.info(str("Profiles selected: " + '%s' % ', '.join(map(str, profiles))))    
        if not profiles:
            logger.error("Please type the profile names correctly in the file config.yaml before running this bot! Exiting bot..")
            os._exit(0)
    
    if enable_multiaccount != False:
        # Get all windows opens
        windows = Desktop(backend="uia").windows()
        window = [w.window_text() for w in windows]
        # Create a dataframe in order to store the windows needed
        df_windows = pd.DataFrame(window, columns =['WebBrowser'])
        # Filter dataframe only to show all windows from Brave web browser
        df_windows = df_windows.loc[df_windows['WebBrowser'].str.contains("Brave", case=False)]
        # Add column key to find profile
        df_windows['Key'] = df_windows['WebBrowser'].str.replace(' ','').str.strip()
        # Add column profile from Brave
        df_windows['Profile'] = df_windows['Key'].str.split('Bombcrypto-Brave').str[1].str.replace(':','').str.replace('-','').str.strip()
        # Add column about the website open from Brave
        df_windows['Website'] = df_windows['WebBrowser'].str.split().str[0].str.strip()
        # Filter dataframe only to show all bombcrypto game window
        df_windows = df_windows.loc[df_windows['Website'] == 'Bombcrypto']
        
        applications = []
        website_browser = []

        try:
            for profile in df_windows['Profile']:
                if profile in profiles:
                    website = df_windows.loc[df_windows.Profile==profile,'WebBrowser'].values[0]                
                    applications.append([website, profile])

            bomb = df_windows.loc[df_windows.Website=='Bombcrypto','Website'].values[0]
            website_browser.append(bomb)
        except:
            pass
        
        return applications, website_browser
    else:
        applications = [['Bot', 'BCOIN', 'None']]
        website_browser = ['Bombcrypto']
        return applications, website_browser

async def create_bat_file():
    try:
        if create_bat != False:
            path = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'bot.bat')
            with open(path, 'w+') as f:
                f.write('cd ' + os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve()) + '\n')
                f.write('python main.py')
            f.close()
            logger = setup_logger(telegram_integration=True)
            logger.info('Bot.bat file created at ' + os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve()))
    except:
        pass

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