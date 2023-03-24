## FLUFFY BUBBLES DISCORD BOT

This discord bot is intended to be used during the VandyHacks discord server / Vanderbilt Universities hackathon event

This bot is templated off of https://github.com/kkrypt0nn/Python-Discord-Bot-Template

To get started, make sure you have git and python3 installed,
then simply clone this repository using `git clone https://github.com/VandyHacks/fluffy-bubbles`

Install all the dependencies using `python -m pip install -r requirements.txt`

After that make sure to create a discord bot and a new file called `config.json` (refer to `sample_config.json`)

* Create a discord bot [here](https://discord.com/developers/applications)
* Get your bot token
* Invite your bot on servers using the following invite:
  https://discord.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot+applications.commands&permissions=PERMISSIONS (
  Replace `YOUR_APPLICATION_ID_HERE` with the application ID and replace `PERMISSIONS` with the required permissions
  your bot needs that it can be get at the bottom of a this
  page https://discord.com/developers/applications/YOUR_APPLICATION_ID_HERE/bot)


How config.json is set up:

| Variable                  | What it is                                                            |
| ------------------------- | ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE      | The prefix you want to use for normal commands                        |
| YOUR_BOT_TOKEN_HERE       | The token of your bot                                                 |
| YOUR_BOT_PERMISSIONS_HERE | The permissions integer your bot needs when it gets invited           |
| YOUR_APPLICATION_ID_HERE  | The application ID of your bot                                        |
| OWNERS                    | The user ID of all the bot owners                                     |

You can now run the program by typing:
```
python bot.py
```