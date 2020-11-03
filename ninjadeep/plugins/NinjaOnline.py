# Copyright ninjadeep
# For @ninjadeepSUPPORT coded by @Lovedeep-ViRk
# Kangers keep credits else I'll take down 🧐

import random
import sys

from telethon import version

from ninjadeep import ALIVE_NAME
from ninjadeep.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ninjadeep User"

ONLINESTR = [
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**NinjaDeep is online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Lovedeep ViRk 🇮🇳](tg://user?id=1324185738 \n\n**More help -** @NinjaDeepSUPPORT \n\n           [🚧 GitHub Repository 🚧](https://github.com/Lovedeep-ViRk/NinjaDeep)",
    f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to NinjaDeep**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @ninjadeepHelpChat \n\n✔️ Created by: [Aditya 🇮🇳](tg://user?id=719195224) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [🌟 Github repository 🌟](https://github.com/Lovedeep-ViRk/NinjaDeep)",
]


@ninjadeep.on(admin_cmd(outgoing=True, pattern="NinjaOnline"))
@ninjadeep.on(sudo_cmd(allow_sudo=True, pattern="NinjaOnline"))
async def NinjaOnline(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await eor(event, random.choice(ONLINESTR))
