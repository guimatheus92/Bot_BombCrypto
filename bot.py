import pyautogui
import os
import pathlib
import asyncio
import numpy as np
from random import randint
from datetime import datetime
from controllers import setup_logger, take_screenshot, read_configurations, run_once

try:
    streamConfig = read_configurations()
    work_heroes_options = streamConfig['heroes_options']['work_heroes_options']
    enable_login_metamask = streamConfig['bot_options']['metamask_options']['enable_login_metamask']
    metamask_password = streamConfig['bot_options']['metamask_options']['metamask_password']    
except FileNotFoundError:
    print('Error: config.yaml file not found, make sure config.yaml are placed in the folder..')
    exit()

async def connect_wallet():
    '''
    Function to connect into wallet, it's the first step of the bot.
    '''    

    #print("Function: " + str(inspect.stack()[0][3]))
    await asyncio.sleep(np.random.uniform(2.5,3.5))

    logger = await asyncio.create_task(setup_logger())
    logger.info('Checking if needs to connect wallet..')
    
    ConnectWalletBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'connect-wallet-btn.png')
    if pyautogui.locateOnScreen(ConnectWalletBtnImg, grayscale=True, confidence=0.8) != None:
        # The connect button is visible        
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(ConnectWalletBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
        # Click on connect button
        pyautogui.click()
        logger = await asyncio.create_task(setup_logger(telegram_integration=True))
        logger.info('Connect wallet button clicked..')
        await asyncio.sleep(np.random.uniform(4.5,5.5))
        return
    
    return

async def open_metamask():
    '''
    Function to open Metamask only.
    '''

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
            logger = await asyncio.create_task(setup_logger(telegram_integration=True))
            logger.info('Metamask icon clicked..')
            await asyncio.sleep(np.random.uniform(2.5,3.5))
            return

async def unlock_metamask():
    '''
    Function to only unlock Metamask.
    The options comes from the yaml file.
    '''

    logger = await asyncio.create_task(setup_logger(telegram_integration=True))
    image_list = ['unlock-btn.png', 'desbloquear-btn.png', 'unlock-btn2.png']
    for unlock_image in image_list:
        UnlockBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', unlock_image)
        # The unlock button is visible
        if pyautogui.locateOnScreen(UnlockBtnImg, grayscale=True, confidence=0.8) != None:
            if enable_login_metamask != False:
                image_list = ['password-tittle.png', 'password-tittle2.png', 'senha-title.png', 'senha-title2.png']                
                for password_img in image_list:
                    PasswordImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', password_img)
                    if pyautogui.locateOnScreen(PasswordImg, grayscale=True, confidence=0.8) != None:
                        await asyncio.sleep(np.random.uniform(1.5,2.5))
                        # Move mouse in a random place first
                        move_mouse_random()
                        # Move to location
                        pyautogui.moveTo(pyautogui.locateOnScreen(PasswordImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
                        # Click on sign button            
                        pyautogui.click()
                        # Write password to unlock Metamask
                        pyautogui.write(metamask_password, interval=0.05)
                        # Move to location
                        pyautogui.moveTo(pyautogui.locateOnScreen(UnlockBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
                        # Click on sign button
                        pyautogui.click()
                        #logger.info('Metamask unlocked..')
                        await asyncio.sleep(np.random.uniform(2.5,3.5))
                        IncorrectPasswordImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'incorrect-password.png')
                        if pyautogui.locateOnScreen(IncorrectPasswordImg, grayscale=True, confidence=0.8) != None:
                            logger.error('Password is wrong, remeber to change on the "metamask_password" option from .yaml file! Exiting bot because it cannot unlock Metamask with the given password..')
                            exit()
                        image_list = ['connected-title.png', 'conectado-title.png']
                        for connectImg in image_list:
                            ConnectImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', connectImg)
                            if pyautogui.locateOnScreen(ConnectImg, grayscale=True, confidence=0.8) != None:
                                logger.info('Password correct, Metamask unlocked succesfully!')
                                # Open Metamask icon
                                await asyncio.create_task(open_metamask())
                                return
            elif enable_login_metamask != True:
                logger.warning('The "enable_login_metamask" option is set to False, so it is not possible to unlock Metamask automatically, unless you change the option to True. Unlock Metamask manually first! Exiting bot..')
                exit()

async def agree_metamask():
    '''
    Function to agree with Metamask, it requires to open the Metamask icon and then signin or unlock Metamask account.
    '''    

    # Click on next button
    image_list = ['proximo-btn.png', 'next-btn.png']
    for next_image in image_list:        
        NextBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', next_image)
        # The next button is visible
        if pyautogui.locateOnScreen(NextBtnImg, grayscale=True, confidence=0.8) != None:
            await asyncio.sleep(np.random.uniform(1.5,2.5))                
            # Move mouse in a random place first
            move_mouse_random()
            # Move to location               
            pyautogui.moveTo(pyautogui.locateOnScreen(NextBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
            # Click on next button
            pyautogui.click()
            logger = await asyncio.create_task(setup_logger(telegram_integration=True))
            logger.info('Metamask connected..')
            # Close Metamask window
            pyautogui.hotkey('esc')
            await asyncio.sleep(np.random.uniform(3.5,4.5))
            return    

async def signin_metamask():
    '''
    Function to sign in into Metamask.    
    '''

    image_list = ['assinar-btn.png', 'sign-btn.png']
    for sign_image in image_list:
        SignBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', sign_image)
        # The sign button is visible
        if pyautogui.locateOnScreen(SignBtnImg, grayscale=True, confidence=0.8) != None:
            await asyncio.sleep(np.random.uniform(1.5,2.5))
            # Move mouse in a random place first
            move_mouse_random()
            # Move to location
            pyautogui.moveTo(pyautogui.locateOnScreen(SignBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
            # Click on sign button            
            pyautogui.click()
            logger = await asyncio.create_task(setup_logger(telegram_integration=True))
            logger.info('Metamask signed..')
            # Close Metamask window
            pyautogui.hotkey('esc')
            await asyncio.sleep(np.random.uniform(3.5,4.5))
            return

async def login_metamask():
    '''
    Function to login into Metamask, it requires to open the Metamask icon and then signin or unlock Metamask account.
    '''

    logger = await asyncio.create_task(setup_logger())
    logger.info('Checking if need to login in Metamask..')

    # Open Metamask icon
    await asyncio.create_task(open_metamask())

    # Unlock Metamask
    await asyncio.create_task(unlock_metamask())    

    # Unlock Metamask
    await asyncio.create_task(agree_metamask())

    # Unlock Metamask
    await asyncio.create_task(signin_metamask())

    return
    

async def treasure_hunt_game(refresh_only=False):
    '''
    Function to go the Treasure Hunt game mode.
    '''

    logger = await asyncio.create_task(setup_logger())
    logger.info('Checking if Treasure Hunt game mode is available..')

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
        logger = await asyncio.create_task(setup_logger(telegram_integration=True))
        logger.info('Treasure Hunt game mode clicked..')
        await asyncio.sleep(np.random.uniform(1.5,2.5))
        if refresh_only != True:
            await asyncio.create_task(send_heroes_to_work())            
        return True
        
async def new_map():
    '''
    Function to check for a new map available
    The game doesn't wait the user to click on the New Map button anymore.
    '''

    logger = await asyncio.create_task(setup_logger())
    logger.info('Checking if is there any new map..')    

    NewMapBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'new-map-btn.png')
    if pyautogui.locateOnScreen(NewMapBtnImg, grayscale=True, confidence=0.8) != None:
        take_screenshot('screenshot', 'new_map', '_antes')
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(NewMapBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)
        # Click on Treasure Hunt game mode
        pyautogui.click()
        await asyncio.sleep(np.random.uniform(0.5,1.5))
        logger = await asyncio.create_task(setup_logger(telegram_integration=True))
        logger.info('New map available at: ' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        await asyncio.sleep(np.random.uniform(1.5,2.5))
        take_screenshot('screenshot', 'new_map', '_depois')
        return
    return

async def send_heroes_to_work():
    '''
    Function to send heroes to work.
    We can use the options to choose what type of heroes or how many heroes we want to send them to work.
    '''

    logger = await asyncio.create_task(setup_logger(telegram_integration=True))
    logger.info('Calling send heroes to work function..')

    # Go back to menu
    await asyncio.create_task(go_back_menu())
    # Go to heroes menu
    await asyncio.create_task(go_to_heroes())

    # If character screen is available
    CharacterTittleImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'character-tittle.png')
    if pyautogui.locateOnScreen(CharacterTittleImg, grayscale=True, confidence=0.8) != None:
        if work_heroes_options == 'all':
            WorkAllBtn = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'work-all-btn.png')
            if pyautogui.locateOnScreen(WorkAllBtn, confidence=0.8) != None:
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
                await asyncio.create_task(close_button())
                # Go to Treasure Hunt mode
                await asyncio.create_task(treasure_hunt_game(refresh_only=True))
                return True            
            else:
                await asyncio.create_task(close_button())
                # Go to Treasure Hunt mode
                await asyncio.create_task(treasure_hunt_game(refresh_only=True))


async def close_button():
    '''
    Function to recognize the close button image.
    '''

    logger = await asyncio.create_task(setup_logger())
    logger.info('Checking if needs to close any screen open..')

    CloseBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'close-btn.png')
    if pyautogui.locateOnScreen(CloseBtnImg, grayscale=True, confidence=0.8) != None:    
        # Move mouse in a random place first
        move_mouse_random()
        # Move to location               
        pyautogui.moveTo(pyautogui.locateOnScreen(CloseBtnImg, grayscale=True, confidence=0.8), None, np.random.uniform(0.4,0.9), pyautogui.easeInOutQuad)    
        # Click on close
        pyautogui.click()        
        logger = await asyncio.create_task(setup_logger(telegram_integration=True))
        logger.info('Close button clicked..')
        await asyncio.sleep(np.random.uniform(0.3,0.9))
        return

async def go_back_menu():
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
        logger = await asyncio.create_task(setup_logger(telegram_integration=True))
        logger.info('Going back to menu..')
        await asyncio.sleep(np.random.uniform(0.5,1.5))
        return True

async def go_to_heroes():
    '''
    Function to recognize the image of heroes from menu and go to the heroes menu.
    From this we can select heroes for work.
    '''

    HeroesImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'heroes-btn.png')
    BuyBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'buy-btn.png')
    logger = await asyncio.create_task(setup_logger(telegram_integration=True))
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

async def refresh_hereoes_positions():
    '''
    Function to refresh heroes positions only.
    From this we can keep the game live without been kicked out.
    '''

    logger = await asyncio.create_task(setup_logger(telegram_integration=True))
    logger.info('Calling refresh heroes function..')

    # Go back to menu
    back = await asyncio.create_task(go_back_menu())
    # Go to heroes menu
    treasure = await asyncio.create_task(treasure_hunt_game(refresh_only=True))

    if back != False and treasure != False:        
        logger.info('Heroes positions refreshed..')

    return

async def first_start():
    
    await asyncio.sleep(np.random.uniform(3.5,5.5))

    # Check some routines before refresh the page

    # Check if treasure hunt mode is already available at screen
    treasure = await asyncio.create_task(treasure_hunt_game(refresh_only=False))

    # Check if is it possible to send heroes to work available at screen
    work = await asyncio.create_task(send_heroes_to_work())

    if treasure != False:
        return
    elif work != False:
        return
    else:
        work = await asyncio.create_task(reload_page())    

async def skip_error_on_game():
    '''
    Function to skip any error on game that might occur.
    It's looking only to an error message, but in case more error appears with different images, we need to add them here.
    '''

    logger = await asyncio.create_task(setup_logger())
    logger.info('Checking if game has any erros or crash..')

    ErrorTittleImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'error-tittle.png')
    ErrorScreenImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'socket-error-screen.png')
    OkBtnImg = os.path.join(os.path.sep, pathlib.Path(__file__).parent.resolve(), 'static', 'img', 'game', 'ok-btn.png')
    logger = await asyncio.create_task(setup_logger(telegram_integration=True))
    if pyautogui.locateOnScreen(ErrorScreenImg, grayscale=True, confidence=0.8) != None:
        # Take screenshot of the error
        take_screenshot('screenshot', 'errors', 'socket')
        await asyncio.sleep(np.random.uniform(0.8,1.5))
        logger.warning('Socket error, check screenshot image to find it..')
        await asyncio.create_task(reload_page())
        await asyncio.create_task(connect_wallet())
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
        await asyncio.create_task(reload_page())
        await asyncio.create_task(connect_wallet())
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

async def reload_page():
    '''
    Function to reload the page by the keys CTRL + F5.
    '''

    # Reload page
    logger = await asyncio.create_task(setup_logger(telegram_integration=True))
    logger.warning('Refreshing the page in order to clear any error if exist..')
    pyautogui.hotkey('ctrl','f5')
    await asyncio.sleep(np.random.uniform(4.5,5.5))
    
    return