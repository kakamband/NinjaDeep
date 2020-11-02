from ninjadeep.utils import admin_cmd


@ninjadeep.on(admin_cmd(outgoing=True, pattern="group"))
@ninjadeep.on(sudo_cmd(allow_sudo=True, pattern="group"))
async def join(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await eor(
            e,
            "This is my community.\n\n[Channel](http://t.me/giveaways_24hrs)\n\n[Chat Group](https://t.me/giveaways24hrsdiscuss)\n\n[UserBot Tutorial - ninjadeep](https://t.me/ninjadeepSUPPORT)\n\n[ninjadeep Chat](https://t.me/NinjaDeepOT)\n\n[Github](https://github.com/Lovedeep-ViRk)",
        )
