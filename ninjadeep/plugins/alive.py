"""Check if your userbot is working."""
import os
import time
from datetime import datetime
from io import BytesIO

import requests
from PIL import Image

from ninjadeep import telever
from ninjadeep.__init__ import StartTime
from ninjadeep.ninjadeepConfig import Config
from ninjadeep.utils import admin_cmd, sudo_cmd

temp = ninjadeep.me
ALIVE_NAME = temp.first_name

ALV_PIC = os.environ.get("ALIVE_PIC", None)

if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@NinjaDeepSUPPORT"


@ninjadeep.on(admin_cmd(outgoing=True, pattern="alive"))
@ninjadeep.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    start = datetime.now()
    myid = bot.uid
    """ For .alive command, check if the bot is running.  """
    end = datetime.now()
    (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    if ALV_PIC:
pm_caption = "➥ **NINJADEEP IS:** `ONLINE`\n\n"
pm_caption += "➥ **SYSTEMS STATS**\n"
pm_caption += "➥ **Telethon Version:** `1.15.0` \n"
pm_caption += "➥ **Python:** `3.8.3` \n"
pm_caption += f"➥ **NinjaDeep Uptime** : `{uptime}` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **NinjaDeep Branch** : `Master`\n"
pm_caption += f"➥ **NinjaDeep Version** : `{telever}`\n"
pm_caption += f"➥ **My Boss** : [{DEFAULTUSER}](tg://user?id={myid}) \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **License** : [GNU General Public License v3.0](github.com/Lovedeep-ViRk/NinjaDeep/blob/master/LICENSE)\n"
pm_caption += "➥ **Copyright** : By [Lovedeep-ViRk@Github](GitHub.com/Lovedeep-ViRk)\n"
pm_caption += "➥ **Check Stats By Doing** `.stat`. \n\n"
pm_caption += "[🇮🇳 Deploy NinjaDeep 🇮🇳](https://github.com/Lovedeep-ViRk/NinjaDeep)"
link_preview=False,


@ninjadeep.on(ninjadeep_on_cmd(pattern=r"alive"))
@ninjadeep.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def ninjadeep(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
         )
        await borg.send_file(alive.chat_id, file=sticker)
        await alive.delete()
