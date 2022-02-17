# BombCrypto Bot

- [en-us] In order to change to english Readme version click [here](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/README.md "here").
- [pt-br] Para alterar para a versão Readme em português, clique [aqui](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/README.pt.md "aqui").

------------

This is an automation (bot) to play the game BombCrypto, it automatically login into the game, send heroes to work, refresh workers, new map, etc.

If you find this bot helpful to you, please donate so we can continue to improve the hard work and hours spent on this 🤯.

![Donation](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/static/img/readme/qr_code.png)

**Donations options:**

- **BUSD/BCOIN/ETH/BNB (BEP20):** 0xf1e43519fca44d9308f889baf99531ed0de903fc
- **PayPal:** https://www.paypal.com/donate/?hosted_button_id=82CABN6CYVG6U
- **Pix:** 42a762ed-e6ec-4059-a88e-f168b9fbc63f (chave aleatória)

## Main Steps

In a breafy way you'll need to:

1. Download `Python`
2. Install python packages from `requirements.txt`
3. Adjust `screen scale` to `100%` if needed
4. Download `Brave` browser (best option)
5. Change options on `config.yaml` file if needed
6. Create `Telegram` bot if needed

## Project structure
    .
    └── Bot_BombCrypto
        ├── main.py                     # setup our app
        ├── bot.py                      # all bot movements
        ├── controllers.py              # all controllers to help the bot to run
        ├── config.yaml                 # all configurations and options to run
        └── logs                        # all log files are saved daily here
        └── static
            ├── img
                ├── game                # all images related to game to run the bot
                ├── readme              # all images related to repository
                ├── screenshot          # all images taken from screenshot (folder will create automatically)

## Tutorial

The tutorial on how to install and use this bot can be found on [GitHub Wiki](https://github.com/guimatheus92/Bot_BombCrypto/wiki/How-to-execute-BombCrypto-bot "GitHub Wiki") page.

The tutorial on how to use Brave browser for this bot can be found on [GitHub Wiki](https://github.com/guimatheus92/Bot_BombCrypto/wiki/How-to-enable-multiaccount-feature-on-Bot "GitHub Wiki") page.

#### Some settings can be changed in the config.yaml file. If you change it, don't forget to restar the bot so that the new settings are activated.

## Changelog

- **16/02/2022**:
    - Minor fixes in some functions
    - Fixed the logging messages

- **10/02/2022**:
    - Added function to send pictures through Telegram

- **02/02/2022**:
    - Updated trigger for each schedule
    
- **27/01/2022**:
    - Added multiaccount features
    - Added bot name in telegram integration
    - Added browser error mechanics due to BombCrypto issue
    - Changed trigger feature based on time
    - Improvement in the cycle of bots

- **24/01/2022**:
 	- Fixed function to get chat_id from telegram
	- Fixed bot when the user doesn't want to use telegram
	- Fixed unlock metamask function
- **19/01/2022**: Released the first version of bot without multiaccount

## Requirements

Browser: `Brave: Version 1.34.81 Chromium: 97.0.4692.99`

#### ⚠️ I really advise you to use the Brave browser instead of others, for so many reasons, especially if you want to use multiaccount feature.

#### For Brave tutorial, check [here](https://github.com/guimatheus92/Bot_BombCrypto/wiki/How-to-enable-multiaccount-feature-on-Bot "here").

------------

Windows version:
- `Windows 10`
- `Windows 11`

Python version:
```python
Python 3.9.9
```

The requirements can be found in `requirements.txt` file also.
This project utilizes the following requirements:

    APScheduler==3.6.3
    asyncio==3.4.3    
    numpy==1.21.4
    opencv-python==4.5.4.60
    pandas==1.1.5
    pathlib==1.0.1
    Pillow==8.4.0
    PyAutoGUI==0.9.53
    python-telegram-bot==13.9
    pywin32==303
    pywinauto==0.6.8
    PyYAML==6.0
    requests==2.26.0
    tzlocal==4.1

Monitor scale: `100%`

## Observations

- Check [Requirements](https://github.com/guimatheus92/Bot_BombCrypto#requirements "Requirements") topic to make sure in what environment, tools and versions we know that it works.
- I suggest you to turn off the feature `News and interests` from Windows, because the mouse might pass through it and click in some card without us know. You can turn off this feature from [Turn news and interests feature on and off](https://support.microsoft.com/en-us/windows/stay-up-to-date-with-news-and-interests-a39baa08-7488-4169-9ed8-577238f46f8f) guide.
- All images taken from the game was from a Full HD screen and scale at 100%. So if your bot is not working, make sure that your scale is at least 100%. After that, get all pictures again and save them as `.png` format.

## Features

- Schedule the refresh of heroes in a period of time
- Schedule sending heroes to work in a period of time
- Delete old files and folders if you want automatically
- Connect into wallet
- Connect, signin, unlock Metamask
- Treasure Hunt game mode
- Check if is there new map available
- Take screenshot of errors and new maps
- Send Telegram message
- Refresh heroes only mode (in case you are playing by yourself)
- Works with as many accounts as you need

###### *Refresh heroes explained: Bot will just refresh the game by going back to menu and then going back to Treasure Hunt mode*

## YAML file configurations and options explained

**1. bot_options**
- **create_logfiles**: You can enable the creation of log in files availabe in the folder `logs`
- **delete_old_logfiles**: You can enable the deletion of old log files and keep today's date file.
- **delete_old_folders**: You can enable the deletion of older folders and keep today's date folders.
- **enable_multiaccount**: You can enable the multiaccount feature.
- **multiaccount_names**: You can set the account/profile names from Brave browser in each line.
- **refresh_browser_time**: You can set the time where the browser will be refreshed by the keys: CTRL + SHIFT + R
**1.1 metamask_options**
	- **enable_login_metamask**: You can enable the login in Metamask when it's locked and needs password to unlock
	- **metamask_password**: If `enable_login_metamask` option is set to `True`, you can pass the password to unlock Metamask.

**2. telegram_options**
- **telegram_integration**: You can enable the integration from log messages to Telegram messages as well
- **telegram_token**: If `telegram_integration` is set to `True`, you can pass the token from your Telegram bot.
- **telegram_chatid**: If `telegram_integration` is set to `True`, you can pass the chat_id number from your Telegram bot. Once the number is wrote, it doesn't change anymore.

**2. heroes_options**
- **work_heroes_options**: You can set the work mode for your heroes. The option `all` send all heroes to work.
- **work_heroes_time**: You can set the time when bot will send them to work automatically.
- **refresh_heroes_time**: You can set the time when bot will just refresh the game by going back to main menu and go to Treasure Hunt game.
- **refresh_heroes_only**: You can enable only the refresh of the game by going back to main menu and go to Treasure Hunt game, with this option the bot *will not* send heroes to work or do other features.

## Improvements

- [X] Some logging messages is not sending when function is called for some reason
- [ ] Send to work some heroes instead of all
- [ ] Send heroes to home
- [X] Send pictures through Telegram message
- [ ] Report on how many times have the main functions run

## Conclusion

1. Want my code? [Grab it here](https://github.com/guimatheus92/Bot_BombCrypto "Grab it here") 📎
2. Want the tutorial of how to use it? [Go to Wiki](https://github.com/guimatheus92/Bot_BombCrypto/wiki "Go to here") ✔️
3. New ideas for this app? Help me to improve it ❤️
4. Want something else added to this tutorial? Add an issue to the repo ⚠️
