import asyncio
import tzlocal
from bot import connect_wallet, login_metamask, treasure_hunt_game, new_map, skip_error_on_game, refresh_hereoes_positions, send_heroes_to_work, first_start
from controllers import countdown_timer, setup_logger, initialize_pyautogui, read_configurations, delete_log_files, delete_folders
from apscheduler.schedulers.asyncio import AsyncIOScheduler

try:
    streamConfig = read_configurations()
    refresh_heroes_time = streamConfig['heroes_options']['refresh_heroes_time']
    refresh_heroes_only = streamConfig['heroes_options']['refresh_heroes_only']
    work_heroes_time = streamConfig['heroes_options']['work_heroes_time']
except FileNotFoundError:
    print('Error: config.yaml file not found, make sure config.yaml are placed in the folder..')
    exit()

async def main():
    logger = await asyncio.create_task(setup_logger(telegram_integration=True))

    # Init message
    print('\nPress Ctrl-C to quit at anytime!\n' )

    hello_world = """
    #******************************* BombCrypto Bot *********************************#
    #────────────────────────────────────────────────────────────────────────────────#
    #─────██████████████───██████████████─██████──────────██████─██████████████──────#
    #─────██░░░░░░░░░░██───██░░░░░░░░░░██─██░░███────────███░░██─██░░░░░░░░░░██──────#
    #─────██░░██████░░██───██░░██████░░██─██░░░███──────███░░░██─██░░██████░░██──────#
    #─────██░░██──██░░██───██░░██──██░░██─██░░░░███────███░░░░██─██░░██──██░░██──────#
    #─────██░░██████░░████─██░░██──██░░██─██░░░░░░██──███░░░░░██─██░░██████░░████────#
    #─────██░░░░░░░░░░░░██─██░░██──██░░██─██░░░░██████████░░░░██─██░░░░░░░░░░░░██────#
    #─────██░░████████░░██─██░░██──██░░██─██░░░░██─████─██░░░░██─██░░████████░░██────#
    #─────██░░██────██░░██─██░░██──██░░██─██░░░░██──██──██░░░░██─██░░██────██░░██────#
    #─────██░░████████░░██─██░░██████░░██─██░░░░██──────██░░░░██─██░░████████░░██────#
    #─────██░░░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░██──────██░░░░██─██░░░░░░░░░░░░██────#
    #─────████████████████─██████████████─████████──────████████─████████████████────#
    #────────────────────────────────────────────────────────────────────────────────#
    #********************************************************************************#
    #***************** Please donate to help improve the hard work ♥ ****************#
    #********************************************************************************#
    #**** BUSD/BCOIN/ETH/BNB (BEP20): 0xf1e43519fca44d9308f889baf99531ed0de903fc ****#
    #**** PayPal: https://www.paypal.com/donate/?hosted_button_id=82CABN6CYVG6U *****#
    #************* Nubank: https://nubank.com.br/pagar/1jxcl/z5fyuL6S28 *************#
    #****************** Pix: 42a762ed-e6ec-4059-a88e-f168b9fbc63f *******************#
    #********************************************************************************#    
    """

    print(hello_world)
            
    # Initialize pyautogui library
    await asyncio.create_task(initialize_pyautogui())

    # Delete old log files
    await asyncio.create_task(delete_log_files())

    # Delete old folders
    await asyncio.create_task(delete_folders())

    # Countdown timer before start the bot
    await asyncio.create_task(countdown_timer())

    logger.info('------------------- New Execution ----------------\n')
    logger.info('Donate on (BUSD/BCOIN/ETH/BNB (BEP20)): 0xf1e43519fca44d9308f889baf99531ed0de903fc')
    logger.info('Donate on (PayPal): https://www.paypal.com/donate/?hosted_button_id=82CABN6CYVG6U')
    logger.info('Donate on (Nubank): https://nubank.com.br/pagar/1jxcl/z5fyuL6S28')
    logger.info('Donate on (Pix): 42a762ed-e6ec-4059-a88e-f168b9fbc63f')
    logger.info('Starting Bot..... Bot started!')

    if refresh_heroes_only != False:
        logger.info('The "refresh heroes only" option is enable, so only the refresh will work on the bot. If you want bot working the whole process, close the bot and change the option to False!')

    if refresh_heroes_time == work_heroes_time:
        logger.critical('You should set a different time for "refresh_heroes_time" and also send them to work from "work_heroes_time". Otherwise these steps might not start correctly.')        

    # Reloading page before start the bot
    await asyncio.create_task(first_start())

    # Create a scheduler for certain functions
    scheduler = AsyncIOScheduler(timezone=str(tzlocal.get_localzone()))              

    if (refresh_heroes_time*60) > 59:
        logger.info('Scheduling the refresh heroes positions every %s minute(s)!' % (refresh_heroes_time))
        # - Do a full review on games
        scheduler.add_job(refresh_hereoes_positions, 'interval', seconds=(refresh_heroes_time*60), id='1', name='refresh_hereoes_positions', misfire_grace_time=180) 
        
    if len(scheduler.get_jobs()) > 0:
        scheduler.start()

    if refresh_heroes_only != True:
        if (work_heroes_time*60) > 59:
            logger.info('Scheduling the time for heroes to work every %s minute(s)!' % (work_heroes_time))
            # - Send heroes to work
            scheduler.add_job(send_heroes_to_work, 'interval', seconds=(work_heroes_time*60), id='2', name='send_heroes_to_work', misfire_grace_time=300)          

        while True:
            # Steps of this bot:
            # - Connect Wallet on BomberCypto game            
            await asyncio.create_task(connect_wallet())
            # - Login Metamask
            await asyncio.create_task(login_metamask())
            # - Treasure Hunt game mode
            await asyncio.create_task(treasure_hunt_game(refresh_only=False))
            # - New map feature
            await asyncio.create_task(new_map())
            # - Check for errors on game
            await asyncio.create_task(skip_error_on_game())

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(main())
        loop.run_forever()
    except Exception as e:
        print("Exception: " + str(e))
        exit()