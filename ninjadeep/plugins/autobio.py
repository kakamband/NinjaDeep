# AutoBio plugin for ninjadeep
# Using this might lead to ban of your account, use at your own risk.
# Re-Written by @Lovedeep_ViRk

import asyncio
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions

from ninjadeep.utils import admin_cmd

DEL_TIME_OUT = 60


@ninjadeep.on(admin_cmd(pattern="autobio"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f" 📅 {DMY} | This is my bio, i Guess | ⌚️ {HMS}"
        logger.info(bio)
        try:
            await borg(
                functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                    about=bio
                )
            )
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
        # logger.info(r.stringify())
        # await borg.send_message(  # pylint:disable=E0602
        #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
        #     "Successfully Changed Profile Bio"
        # )
        await asyncio.sleep(DEL_TIME_OUT)
