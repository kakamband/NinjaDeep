# NinjaDeep - Telegram UserBot
[NINJADEEP](https://telegra.ph/file/a1467c3b6cafdfee8f6ba.jpg)

# <p align="left"><a href="https://github.com/Lovedeep-ViRk/NinjaDeep"><img src="https://github-readme-stats.vercel.app/api/pin?username=Lovedeep-ViRk&show_icons=true&theme=dark&hide_border=true&repo=NinjaDeep"></a></p><p align="centre"><a href="https://t.me/NinjaDeepOT"> <img src="https://img.shields.io/badge/telegram-Support_Group-blue?style=social&logo=telegram" alt="Support" /></a><a href="https://github.com/Lovedeep-ViRk/NinjaDeep/stargazers"><img src="https://img.shields.io/github/stars/Lovedeep-ViRk/NinjaDeep?style=social"></a><a href="https://github.com/Lovedeep-ViRk/NinjaDeep/fork"><img src="https://img.shields.io/github/forks/Lovedeep-ViRk/NinjaDeep?label=Fork&logoColor=blue&style=social"></a><a href="https://github.com/Lovedeep-ViRk/NinjaDeep"><img src="https://img.shields.io/github/last-commit/Lovedeep-ViRk/NinjaDeep?style=flat-square"></a></p>
   
## The Easier Way to install

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Lovedeep-ViRk/NinjaDeep)

## Support
Join [Support group](https://t.me/NinjaDeepOT) for updates and new plugin suggestions.
Do fork and star the repo 

### Session String 
<a href="https://ninjadeep-sessionstring-generator.lovedeep.repl.run/" target="_blank"><img src="https://img.shields.io/badge/run-string__session.py-red?style=for-the-badge&logo=repl.it" alt="generate_string" /></a>

### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/Lovedeep-ViRk/NinjaDeep
cd NinjaDeep
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```
## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

# Disclaimer
```
/**
    	Improper use may lead to ban.
    	I am not responsible if you misuse this bot.
	This bot is just for managing groups more effectively and having some fun
	with your telegram account.
	No one is responsible for your actions.
	If you spammed and got reported again and again, 
	and, at last got your account banned, and you
	point your fingers at me, I'll be rolling on the floor laughing at you.
Dont Complaint to Lovedeep(CREATOR)  if Ur Account Banned Bcz i give u Disclaimer First......!
/**
```

