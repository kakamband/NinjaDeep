#    ninjadeep - UserBot
#    Copyright (C) 2020 ninjadeep

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

import asyncio

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#    By @Lovedeep_ViRk
#
import os
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions

from ninjadeep import *
from ninjadeep import AUTO_PIC_FONT, AUTOPIC_FONT_COLOUR, AUTOPIC_TEXT

fntz = str(AUTO_PIC_FONT) if AUTO_PIC_FONT else "DejaVuSans.ttf"
FONT_FILE_TO_USE = f"fonts/{fntz}"
AUTOPIC_TEXT = (
    str(AUTOPIC_TEXT)
    if AUTOPIC_TEXT
    else "Life Is too Short.\n And so is your NinjaDeep account."
)
COLOUR = str(AUTOPIC_FONT_COLOUR) if AUTOPIC_FONT_COLOUR else (255, 255, 255)


@ninjadeep.on(admin_cmd(pattern="autopic"))
async def autopic(event):
    await event.edit("**Autopic has been enabled •Succesfully• By NinjaDeep!!!**")
    a = await event.get_reply_message()
    downloaded_file_name = "ninjadeep/original_pic.png"
    await ninjadeep.download_media(a, downloaded_file_name)
    photo = "ninjadeep/photo_pfp.png"
    while True:
        shutil.copy(downloaded_file_name, photo)
        current_time = datetime.now().strftime(
            f"Time: %H:%M \nDate: %d.%m.%y \n{AUTOPIC_TEXT}"
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        color = COLOUR
        drawn_text.text((95, 250), current_time, font=fnt, fill=color)
        img.save(photo)
        file = await event.client.upload_file(photo)
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(photo)
            await asyncio.sleep(60)
        except BaseException:
            return
