#  (c)2020 ninjadeep
#
# You may not use this plugin without proper authorship and consent from @ninjadeepSupport
#
# By @buddhhu, @Itzsjdude
#
import os

from ninjadeep.utils import admin_cmd, sudo_cmd


@ninjadeep.on(admin_cmd(pattern=r"reveal", outgoing=True))
@ninjadeep.on(sudo_cmd(pattern=r"reveal"))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("**Reading file...**")
    if len(c) > 4095:
        await a.edit("`The Total words in this file is more than telegram limits.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
        await a.delete()
    os.remove(b)
