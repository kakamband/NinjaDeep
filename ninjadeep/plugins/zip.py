""" command: .compress """

import asyncio
import os
import zipfile

from uniborg.util import admin_cmd


@ninjadeep.on(admin_cmd(pattern="compress"))
@ninjadeep.on(sudo_cmd(pattern="compress", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_reply:
        await eor(event, "Reply to a file pro saar.")
        return
    mone = await eor(event, "Processing ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        try:
            downloaded_file_name = await borg.download_media(
                reply_message, Config.TMP_DOWNLOAD_DIRECTORY
            )
            directory_name = downloaded_file_name
            await eor(event, downloaded_file_name)
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
    zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
        directory_name
    )
    await borg.send_file(
        event.chat_id,
        directory_name + ".zip",
        caption="Zipped Successfully!",
        force_document=True,
        allow_cache=False,
        reply_to=event.message.id,
    )
    await eor(event, "DONE!!!")
    await asyncio.sleep(7)
    await event.delete()


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))
