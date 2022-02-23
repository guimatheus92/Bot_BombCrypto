import datetime
import pyautogui
import os
import pathlib
import asyncio
import numpy as np
from random import randint
from controllers import setup_logger, take_screenshot, read_configurations, send_telegram_pic

try:
    streamConfig = read_configurations()
    work_heroes_options = streamConfig['heroes_options']['work_heroes_options']
    enable_login_metamask = streamConfig['bot_options']['metamask_options']['enable_login_metamask']
    metamask_password = streamConfig['bot_options']['metamask_options']['metamask_password']
    telegram_integration = streamConfig['telegram_options']['telegram_integration']
except FileNotFoundError:
    print('Error: config.yaml file not found, make sure config.yaml are placed in the folder..')
    exit()

async def connect_wallet(app_name=''):
    '''
    Function to connect into wallet, it's the first step of the bot.
    '''    

    await asyncio.sleep(np.random.uniform(2.5,3.5))

    logger = setup_logger()
    logger.info('Checking if needs to connect wallet..')
    
    ConnectWalletBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'connect-wallet-btn.png')
    ConnectBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'connect-btn.png')

    if pyautogui.locateOnScreen(ConnectWalletBtnImg, grayscale=True, confidence=0.8) != None:
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(ConnectWalletBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
        # Click on connect button
        pyautogui.click()
        if pyautogui.locateOnScreen(ConnectBtnImg, grayscale=True, confidence=0.8) != None:
            # Move mouse in a random place first
            move_mouse_random()
            # Move to location               
            pyautogui.moveTo(pyautogui.locateOnScreen(ConnectBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
            # Click on connect button
            pyautogui.click()
        logger = setup_logger(telegram_integration=True, bot_name=app_name)
        logger.info('Wallet connected!')
        await asyncio.sleep(np.random.uniform(1.5,2.5))
        return

async def open_metamask(app_name=''):
    '''
    Function to open Metamask only.
    '''

    await asyncio.sleep(np.random.uniform(1.5,2.5))
    # Move to a point where it can be clicked without a problem in order to make the Metamask screen disapear 
    pyautogui.moveTo(930, 328, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
    # Click on Metamask icon
    pyautogui.click()    

    image_list = ['metamask-icon-notification-btn.png', 'metamask-icon-notification-btn2.png']
    for metamaskimg in image_list:
        MetamaskBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', metamaskimg)
        if pyautogui.locateOnScreen(MetamaskBtnImg, grayscale=True, confidence=0.8) != None:        
            # Move mouse in a random place first
            move_mouse_random()
            # Move to location
            pyautogui.moveTo(pyautogui.locateOnScreen(MetamaskBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
            # Click on Metamask icon
            pyautogui.click()
            logger = setup_logger(telegram_integration=True, bot_name=app_name)
            logger.info('Metamask icon clicked..')
            await asyncio.sleep(np.random.uniform(0.5,1))
            return

async def unlock_metamask(app_name=''):
    '''
    Function to only unlock Metamask.
    The options comes from the yaml file.
    '''

    logger = setup_logger(telegram_integration=True, bot_name=app_name)
    image_list = ['unlock-btn.png', 'desbloquear-btn.png', 'unlock-btn2.png']
    for unlock_image in image_list:
        UnlockBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', unlock_image)
        # The unlock button is visible
        if pyautogui.locateOnScreen(UnlockBtnImg, confidence=0.8) != None:
            if enable_login_metamask != False:
                image_list = ['password-tittle.png', 'password-tittle2.png', 'senha-title.png', 'senha-title2.png']                
                for password_img in image_list:
                    PasswordImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', password_img)
                    if pyautogui.locateOnScreen(PasswordImg, confidence=0.8) != None:
                        await asyncio.sleep(np.random.uniform(0.8,1.5))
                        # Move mouse in a random place first
                        move_mouse_random()
                        # Move to location
                        pyautogui.moveTo(pyautogui.locateOnScreen(PasswordImg, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
                        # Click on password field
                        pyautogui.click()
                        # Write password to unlock Metamask
                        pyautogui.write(metamask_password, interval=0.05)
                        # Move to location
                        pyautogui.moveTo(pyautogui.locateOnScreen(UnlockBtnImg, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
                        # Click on unlock button
                        pyautogui.click()
                        await asyncio.sleep(np.random.uniform(1.5,2.5))
                        IncorrectPasswordImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'incorrect-password.png')
                        if pyautogui.locateOnScreen(IncorrectPasswordImg, confidence=0.8) != None:
                            logger.error('Password is wrong, remeber to change on the "metamask_password" option from .yaml file! Exiting bot because it cannot unlock Metamask with the given password..')
                            exit()
                        image_list = ['connected-title.png', 'conectado-title.png']
                        for connectImg in image_list:
                            ConnectImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', connectImg)
                            if pyautogui.locateOnScreen(ConnectImg, confidence=0.8) != None:
                                logger.info('Password correct, Metamask unlocked succesfully!')
                                # Open Metamask icon
                                await asyncio.create_task(open_metamask())
                                return                            
            elif enable_login_metamask != True:
                logger.warning('The "enable_login_metamask" option is set to False, so it is not possible to unlock Metamask automatically, unless you change the option to True. Unlock Metamask manually first! Exiting bot..')
                exit()

async def signin_metamask(app_name=''):
    '''
    Function to sign in into Metamask.    
    ''' 
    
    image_list = ['assinar-btn.png', 'sign-btn.png']
    for sign_image in image_list:
        SignBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', sign_image)
        # The sign button is visible
        if pyautogui.locateOnScreen(SignBtnImg, confidence=0.8) != None:
            await asyncio.sleep(np.random.uniform(0.4,0.8))
            # Move mouse in a random place first
            move_mouse_random()
            # Move to location
            pyautogui.moveTo(pyautogui.locateOnScreen(SignBtnImg, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
            # Click on sign button            
            pyautogui.click()
            logger = setup_logger(telegram_integration=True,bot_name=app_name)
            logger.info('Metamask signed..')
            # Close Metamask window
            pyautogui.hotkey('esc')
            await asyncio.sleep(np.random.uniform(14,16))
            await asyncio.create_task(go_to_heroes(app_name=app_name))
            await asyncio.create_task(send_heroes_to_work(app_name=app_name))
            return                

async def login_metamask(app_name=''):
    '''
    Function to login into Metamask, it requires to open the Metamask icon and then signin or unlock Metamask account.
    '''

    logger = setup_logger()
    logger.info('Checking if need to login in Metamask..')

    # Open Metamask icon
    await asyncio.create_task(open_metamask(app_name=app_name))
    # Unlock Metamask
    await asyncio.create_task(unlock_metamask(app_name=app_name))
    # Sign Metamask
    await asyncio.create_task(signin_metamask(app_name=app_name))
    return
    

async def treasure_hunt_game(refresh_only=True, app_name=''):
    '''
    Function to go the Treasure Hunt game mode.
    '''

    logger = setup_logger(telegram_integration=False, bot_name=app_name)
    logger.info('Checking if Treasure Hunt game mode is available..')

    TreasureHuntImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'treasure-hunt-screen.png')
    await asyncio.sleep(np.random.uniform(2.5,3.5))
    if pyautogui.locateOnScreen(TreasureHuntImg, grayscale=True, confidence=0.8) != None:
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(TreasureHuntImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
        # Click on Treasure Hunt game mode
        pyautogui.click()
        await asyncio.sleep(np.random.uniform(0.5,1.5))
        logger = setup_logger(telegram_integration=True,bot_name=app_name)
        logger.info('Treasure Hunt game mode clicked..')
        await asyncio.sleep(np.random.uniform(1.5,2.5))
        if refresh_only != True:
            await asyncio.create_task(send_heroes_to_work(app_name=app_name))            
        return True
        
async def new_map(app_name=''):
    '''
    Function to check for a new map available
    The game doesn't wait the user to click on the New Map button anymore.
    '''

    logger = setup_logger(telegram_integration=False, bot_name=app_name)
    logger.info('Checking if is there any new map..')

    NewMapBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'new-map-btn.png')
    if pyautogui.locateOnScreen(NewMapBtnImg, grayscale=True, confidence=0.8) != None:
        take_screenshot('screenshot', 'new_map', 'antes')
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(NewMapBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
        # Click on Treasure Hunt game mode
        pyautogui.click()
        await asyncio.sleep(np.random.uniform(0.5,1.5))
        logger = setup_logger(telegram_integration=True, bot_name=app_name)
        logger.info('New map available at: ' + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        await asyncio.sleep(np.random.uniform(1.5,2.5))
        take_screenshot('screenshot', 'new_map', 'depois')
        return

async def send_heroes_to_work(app_name=''):
    '''
    Function to send heroes to work.
    We can use the options to choose what type of heroes or how many heroes we want to send them to work.
    '''

    logger = setup_logger(telegram_integration=False, bot_name=app_name)
    logger.info('Checking if needs to send heroes to work..')

    # Go back to menu
    await asyncio.create_task(go_back_menu(app_name=app_name))
    # Go to heroes menu
    await asyncio.create_task(go_to_heroes(app_name=app_name))

    # If character screen is available
    CharacterTittleImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'character-tittle.png')
    if pyautogui.locateOnScreen(CharacterTittleImg, grayscale=True, confidence=0.8) != None:
        logger = setup_logger(telegram_integration=True,bot_name=app_name)
        logger.info('[Work] Calling send heroes to work function..')
        if work_heroes_options == 'all':
            WorkAllBtn = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'work-all-btn.png')
            if pyautogui.locateOnScreen(WorkAllBtn, confidence=0.8) != None:
                # Take Screenshot
                path_file = take_screenshot('screenshot', 'report', 'sendheroestowork')
                await asyncio.sleep(np.random.uniform(0.8,1.5))
                # Send picture to Telegram
                send_telegram_pic(path_file)
                # Move mouse in a random place first
                move_mouse_random()
                # Move to location
                pyautogui.moveTo(pyautogui.locateOnScreen(WorkAllBtn, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
                # Click on Treasure Hunt game mode
                pyautogui.click()
                await asyncio.sleep(np.random.uniform(0.5,1.5))              
                logger.info('All heroes were sending to work..')
                await asyncio.sleep(np.random.uniform(1.5,2.5))
                # Close the window for heroes
                await asyncio.create_task(close_button(app_name=app_name))
                # Go to Treasure Hunt mode
                await asyncio.create_task(treasure_hunt_game(refresh_only=True,app_name=app_name))
                return True            
            else:
                await asyncio.create_task(close_button(app_name=app_name))
                # Go to Treasure Hunt mode
                await asyncio.create_task(treasure_hunt_game(refresh_only=True,app_name=app_name))
                return


async def close_button(app_name=''):
    '''
    Function to recognize the close button image.
    '''

    logger = setup_logger(telegram_integration=False, bot_name=app_name)
    logger.info('Checking if needs to close any screen open..')

    CloseBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'close-btn.png')
    if pyautogui.locateOnScreen(CloseBtnImg, grayscale=True, confidence=0.8) != None:    
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(CloseBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)    
        # Click on close
        pyautogui.click()        
        logger = setup_logger(telegram_integration=True,bot_name=app_name)
        logger.info('Close button clicked..')
        await asyncio.sleep(np.random.uniform(0.3,0.9))
        return

async def go_back_menu(app_name=''):
    '''
    Function to recognize the image of the arrow button and go back to the main menu.
    From this we can select the game mode or go anywhere we want from the game.
    '''

    BackMenuImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'go-back-arrow-btn.png')
    # Go back on arrow button
    if pyautogui.locateOnScreen(BackMenuImg, grayscale=True, confidence=0.8) != None:
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(BackMenuImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad) 
        # Click on Treasure Hunt game mode
        pyautogui.click()
        await asyncio.sleep(np.random.uniform(0.5,1.5))
        logger = setup_logger(telegram_integration=True, bot_name=app_name)
        logger.info('Going back to menu..')
        await asyncio.sleep(np.random.uniform(0.5,1.5))
        return True

async def go_to_heroes(app_name=''):
    '''
    Function to recognize the image of heroes from menu and go to the heroes menu.
    From this we can select heroes for work.
    '''

    HeroesImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'heroes-btn.png')
    BuyBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'buy-btn.png')
    logger = setup_logger(telegram_integration=True,bot_name=app_name)
    if pyautogui.locateOnScreen(HeroesImg, grayscale=True, confidence=0.8) != None:
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(HeroesImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
        # Click on Treasure Hunt game mode
        pyautogui.click()
        await asyncio.sleep(np.random.uniform(0.5,1.5))
        logger.info('Going to heroes menu..')
        await asyncio.sleep(np.random.uniform(2.5,3.5))        
        if pyautogui.locateOnScreen(BuyBtnImg, grayscale=True, confidence=0.8) != None:
            logger.error('Account without heroes, you need to buy a heroe first, before running this bot! Exiting bot..')
            exit()
        return True    

async def refresh_hereoes_positions(app_name=''):
    '''
    Function to refresh heroes positions only.
    From this we can keep the game live without been kicked out.
    '''

    logger = setup_logger(telegram_integration=False, bot_name=app_name)
    logger.info('Checking if needs to refresh the game..')

    # Go back to menu
    BackMenuImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'go-back-arrow-btn.png')
    # Go back on arrow button
    if pyautogui.locateOnScreen(BackMenuImg, grayscale=True, confidence=0.8) != None:
        logger = setup_logger(telegram_integration=True, bot_name=app_name)
        logger.info('[Refresh] Calling refresh heroes position function..')        
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(BackMenuImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad) 
        # Click on Treasure Hunt game mode
        pyautogui.click()
        await asyncio.sleep(np.random.uniform(0.5,1.5))        
        logger.info('Going back to menu..')
        await asyncio.sleep(np.random.uniform(0.5,1.5))        

    # Go to heroes menu
    TreasureHuntImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'treasure-hunt-screen.png')
    await asyncio.sleep(np.random.uniform(2.5,3.5))
    if pyautogui.locateOnScreen(TreasureHuntImg, confidence=0.8) != None:
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(TreasureHuntImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
        # Click on Treasure Hunt game mode
        pyautogui.click()
        await asyncio.sleep(np.random.uniform(0.5,1.5))
        logger.info('Treasure Hunt game mode clicked..')
        await asyncio.sleep(np.random.uniform(1.5,2.5))

        logger.info('Heroes positions refreshed..')

    return

async def first_start(app_name=''):
    
    await asyncio.sleep(np.random.uniform(3.5,5.5))

    logger = setup_logger(telegram_integration=True, bot_name=app_name)
    logger.info('First start function..')

    # Check some routines before refresh the page

    # Refresh page if game is not already logged
    BombCryptoImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'bombcrypto-screen.png')
    if pyautogui.locateOnScreen(BombCryptoImg, grayscale=True, confidence=0.8) != None:
        await asyncio.create_task(reload_page(app_name=app_name))

    # Check if treasure hunt mode is already available at screen
    await asyncio.create_task(treasure_hunt_game(refresh_only=False, app_name=app_name))

    # Check if is it possible to send heroes to work available at screen
    await asyncio.create_task(send_heroes_to_work(app_name=app_name))

    # Check if is it possible to send heroes to work available at screen
    await asyncio.create_task(how_many_coins(app_name=app_name))    

    logger.info('Exiting start function..')

async def skip_error_on_game(app_name=''):
    '''
    Function to skip any error on game that might occur.
    It's looking only to an error message, but in case more error appears with different images, we need to add them here.
    '''

    logger = setup_logger(telegram_integration=False, bot_name=app_name)
    logger.info('Checking if game has any erros or crash..')

    ErrorTittleImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'error-tittle.png')
    ErrorScreenImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'socket-error-screen.png')
    BrowserErrorBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'browser-error.png')
    OkBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'ok-btn.png')
    logger = setup_logger(telegram_integration=True,bot_name=app_name)
    if pyautogui.locateOnScreen(ErrorScreenImg, grayscale=True, confidence=0.8) != None:
        # Take screenshot of the error
        take_screenshot('screenshot', 'errors', 'socket')
        await asyncio.sleep(np.random.uniform(0.8,1.5))
        logger.warning('Socket error, check screenshot image to find it..')
        await asyncio.create_task(reload_page(app_name=app_name))
        return
    elif pyautogui.locateOnScreen(BrowserErrorBtnImg, grayscale=True, confidence=0.8) != None:
        # Take screenshot of the error
        take_screenshot('screenshot', 'errors', 'browser_error')
        await asyncio.sleep(np.random.uniform(0.8,1.5))
        logger.warning('Browser error, check screenshot image to find it..')
        if pyautogui.locateOnScreen(BrowserErrorBtnImg, grayscale=True, confidence=0.8) != None:
            # Move mouse in a random place first
            move_mouse_random()
            # Move to location               
            pyautogui.moveTo(pyautogui.locateOnScreen(BrowserErrorBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
            # Click on button
            pyautogui.click()
        # Start game again
        await asyncio.create_task(reload_page(app_name=app_name))
        return
    elif pyautogui.locateOnScreen(ErrorTittleImg, grayscale=True, confidence=0.8) != None:
        # Take screenshot of the error
        take_screenshot('screenshot', 'errors')
        await asyncio.sleep(np.random.uniform(0.8,1.5))
        logger.warning('Error on game, check screenshot image to find it..')
        # Check if OK button is available
        if pyautogui.locateOnScreen(OkBtnImg, grayscale=True, confidence=0.8) != None:
            # Move mouse in a random place first
            move_mouse_random()
            # Move to location               
            pyautogui.moveTo(pyautogui.locateOnScreen(OkBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
            # Click on button
            pyautogui.click()
        # Start game again
        await asyncio.create_task(reload_page(app_name=app_name))
        return

async def how_many_coins(app_name=''):
    '''
    Function to send screenshot to telegram of how many coins the player has.
    '''
    
    ChestImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'chest-btn.png')
    logger = setup_logger(telegram_integration=True,bot_name=app_name)
    if pyautogui.locateOnScreen(ChestImg, grayscale=True, confidence=0.8) != None:
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location
        pyautogui.moveTo(pyautogui.locateOnScreen(ChestImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
        # Click on button
        pyautogui.click()
        await asyncio.sleep(np.random.uniform(0.5,0.8))
        # Take screenshot of the error
        path_file = take_screenshot('screenshot', 'report', 'coins')
        # Send picture to Telegram
        send_telegram_pic(path_file)
        logger.info('Screenshot took from chest, you can check how many coins you have!')
        await asyncio.create_task(close_button(app_name=app_name))
        return


def move_mouse_random():
    '''
    Function to move mouse in a random place.
    '''

    # Get the size of the screen
    screen_width , screen_height = pyautogui.size()

    x = randint(0, screen_width - 1)
    y = randint(0, screen_height -1)
 
    #print("Moving to ({},{})".format(x,y))
    pyautogui.moveTo(x,y, duration=0.50)

async def reload_page(app_name=''):
    '''
    Function to reload the page by the keys CTRL + F5.
    '''

    # Reload page
    logger = setup_logger(telegram_integration=True, bot_name=app_name)
    logger.warning('[Reload] Reloading the page in order to clear any error if exist..')
    pyautogui.hotkey('ctrl','shift', 'r')
    await asyncio.sleep(np.random.uniform(4.5,5.5))
    
    return

class SetTrigger(object):
    def __init__(self):
        self.set_work = False
        self.set_reload = False
        self.set_refresh = False
        self.set_coin = False
    
    def UpdateSetRefresh(self):
        self.set_refresh = True
        return self.set_refresh

    def UpdateSetWork(self):
        self.set_work = True
        return self.set_work

    def UpdateSetReload(self):
        self.set_reload = True
        return self.set_reload
    
    def UpdateSetCoin(self):
        self.set_coin = True
        return self.set_coin