# Ported from other Telegram UserBots for NinjaDeep//Made for NinjaDeep
# Kangers, don't remove this line
# @Lovedeep_ViRk

"""Available Commands:
.info
"""

import asyncio

from ninjadeep.utils import admin_cmd


@ninjadeep.on(admin_cmd(pattern="info"))
@ninjadeep.on(sudo_cmd(pattern="info", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 36)
    # input_str = event.pattern_match.group(1)
    # if input_str == "Visit this page to know more about NinjaDeep.":
    await eor(event, "Thanks")
    animation_chars = ["**ninjadeep**", "[More Info](https://t.me/NinjaDeepOT)"]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await eor(event, animation_chars[i % 18])
