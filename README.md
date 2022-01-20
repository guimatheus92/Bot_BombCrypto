# BombCrypto Bot

- [en-us] For change to english Readme version click [here](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/README.md "here").
- [pt-br] Para alterar para a versão Readme em português, clique [aqui](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/README.pt.md "aqui").

------------

This is an automation (bot) to play the game BombCrypto, it automatically login into the game, send heroes to work, refresh workers, new map, etc.

If you find this bot helpful to you, please donate so we can continue to improve the hard work and hours spent on this 🤯.

![Donation](https://github.com/guimatheus92/Bot_BombCrypto/blob/main/static/img/readme/qr_code.png)

**Donations options:**

- **BUSD/BCOIN/ETH/BNB (BEP20):** 0xf1e43519fca44d9308f889baf99531ed0de903fc
- **PayPal:** https://www.paypal.com/donate/?hosted_button_id=82CABN6CYVG6U
- **Pix:** 42a762ed-e6ec-4059-a88e-f168b9fbc63f (chave aleatória)

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

## Tutorial

The tutorial on how to install and use this bot can be found on [GitHub Wiki](https://github.com/guimatheus92/Bot_BombCrypto/wiki/How-to-execute-BombCrypto-bot "GitHub Wiki") page.

##### Some settings can be changed in the config.yaml file. If you change it, don't forget to restar the bot so that the new settings are activated.

## Changelog

- **19/01/2022**: Released the first version of bot without multiaccount

## Requirements

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
    numpy==1.21.4
    PyAutoGUI==0.9.53
    python-telegram-bot==13.9
    pywin32==303
    pywinauto==0.6.8
    PyYAML==6.0
    requests==2.26.0
    tzlocal==4.1

Monitor scale: `100%`

## Observations

- Check [Requirements](https://github.com/guimatheus92/Bot_BombCrypto#requirements "Requirements") topic to make sure in what environment and versions we know that it works.
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

###### *Refresh heroes explained: Bot will just refresh the game by going back to menu and then going back to Treasure Hunt mode*

## Conclusion

1. Want my code? [Grab it here](https://github.com/guimatheus92/Bot_BombCrypto "Grab it here") 📎
2. Want the tutorial of how to use it? [Go to Wiki](https://github.com/guimatheus92/Bot_BombCrypto/wiki/How-to-execute-BombCrypto-bot "Go to here") ✔️
3. New ideas for this app? Help me to improve it ❤️
4. Want something else added to this tutorial? Add an issue to the repo ⚠️
