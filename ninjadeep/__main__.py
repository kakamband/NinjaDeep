import glob
from ninjadeep import bot
from sys import argv
from telethon import TelegramClient
from ninjadeep.ninjadeepConfig import Var
from ninjadeep.utils import load_module, start_mybot
from pathlib import Path
import telethon.utils
from ninjadeep import CMD_HNDLR

TELE = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    await bot.send_message(TELE, f"**`NinjaDeep has been deployed`,** @{BOTNAME} **has been set up.\nSend** `{CMD_HNDLR}alive` **to see if the bot is working.\n\n__Do add** @{BOTNAME} **to this group and make it admin for enabling all the features of NinjaDeep.**__")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting NinjaDeep")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = 'ninjadeep/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

print("NinjaDeep has been deployed! ")

print("Setting up NinjaTGBot")

path = "ninjadeep/plugins/mybot/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_mybot(shortname.replace(".py", ""))

print("NinjaTGBot has been set up!")
print("NinjaDeep has been fully deployed! Do Visit @NinjaDeepOT")
bot.loop.run_until_complete(startup_log_all_done())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
