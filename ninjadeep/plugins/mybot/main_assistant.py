#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import io
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from ninjadeep import bot
from ninjadeep.plugins.sql_helper.blacklist_admin import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from ninjadeep.plugins.sql_helper.botusers_sql import add_me_in_db, his_userid
from ninjadeep.plugins.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)


@admin_cmd("start", is_args=False)
async def start(event):
    deepbot = await tgbot.get_me()
    bot_id = deepbot.first_name
    bot_username = deepbot.username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    vent = event.chat_id
    starttext = f"Hello, {firstname} ! Nice To Meet You, Well I Am {bot_id}, An Powerfull admin Bot. \n\nMy [➤ Master](tg://user?id={bot.uid}) \nYou Can Talk/Contact My Master Using This Bot. \n\nIf You Want Your Own admin You Can Deploy From Button Below. \n\nPowered By [NinjaDeep🇮🇳](t.me/NinjaDeepOT)",
    buttons=[
         [Button.url("CREATOR👑", "t.me/Lovedeep_ViRk")],
         ],
       )
    if event.sender_id == bot.uid:
        await tgbot.send_message(
            vent,
            message=f"Hi Master, It's Me {bot_id}, Your admin ! \nWhat You Wanna Do today ?",
            buttons=[
                [custom.Button.inline("Show Users 🔥", data="users")],
                [custom.Button.inline("Commands For admin", data="gibcmd")],
                [
                    Button.url(
                        "Add Me to Group 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await tgbot.send_message(
            event.chat_id,
            message=starttext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("Deploy your NinjaDeep 🇮🇳", data="deploy")],
                [Button.url("Help Me ❓", "t.me/NinjaDeepot")],
           ],
        )


# Data's


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deploy")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="You Can Deploy NinjaDeep In Heroku By Following Steps Bellow, You Can See Some Quick Guides On Support Channel Or On Your Own NinjaDeep admin Bot. \nThank You For Contacting Me.",
            buttons=[
                [Button.url("Heroku", "https://heroku.com")],
                [Button.url("Need Help ❓", "t.me/NinjaDeepSupport")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    if event.query.user_id == bot.uid:
        await event.delete()
        total_users = get_all_users()
        users_list = "List Of Total Users In Bot. \n\n"
        for deeped in total_users:
            users_list += ("==> {} \n").format(int(deeped.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await tgbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="Total Users In Your Bot.",
                allow_cache=False,
            )
    else:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gibcmd")))
async def users(event):
    await event.delete()
    grabon = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await tgbot.send_message(event.chat_id, grabon)


# Bot Permit.
@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def all_messages_catcher(event):
    if is_he_added(event.sender_id):
        return
    if event.raw_text.startswith("/"):
        pass
    elif event.sender_id == bot.uid:
        return
    else:
        await event.get_sender()
        event.chat_id
        sed = await event.forward_to(bot.uid)
        # Add User To Database ,Later For Broadcast Purpose
        # (C) @SpecHide
        add_me_in_db(sed.id, event.sender_id, event.id)


@tgbot.on(events.NewMessage(func=lambda e: e.is_private))
async def sed(event):
    msg = await event.get_reply_message()
    if msg is None:
        return
    msg.id
    msg_s = event.raw_text
    user_id, reply_message_id = his_userid(msg.id)
    if event.sender_id == Config.OWNER_ID:
        if event.raw_text.startswith("/"):
            return
        if event.text is not None and event.media:
            bot_api_file_id = pack_bot_file_id(event.media)
            await tgbot.send_file(
                user_id,
                file=bot_api_file_id,
                caption=event.text,
                reply_to=reply_message_id,
            )
        else:
            msg_s = event.raw_text
            await tgbot.send_message(
                user_id,
                msg_s,
                reply_to=reply_message_id,
            )


@admin_cmd("broadcast", is_args=True)
@god_only
async def sedlyfsir(event):
    msgtobroadcast = event.pattern_match.group(1)
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    for deepcast in userstobc:
        try:
            sent_count += 1
            await tgbot.send_message(int(deepcast.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except Exception as e:
            try:
                logger.info(f"Error : {error_count}\nError : {e} \nUsers : {chat_id}")
            except:
                pass
    await tgbot.send_message(
        event.chat_id,
        f"Broadcast Done in {sent_count} Group/Users and I got {error_count} Error and Total Number Was {len(userstobc)}",
    )


@admin_cmd("stats", is_args=False)
@peru_only
async def deepvirk(event):
    deepvirk = get_all_users()
    await event.reply(
        f"**tele = f"NinjaDeep Version: {ninja_version}\n"
tele += f"Log Group: {log}\n"
tele += f"admin Bot: {bots}\n"
tele += f"Lydia: {lyd}\n"
tele += f"Sudo: {sudo}\n"
tele += f"PMSecurity: {pm}\n"
tele += f"\nVisit @NinjaDeepSupport for assistance.\n"
telestats = f"{tele}"
    )


@admin_cmd("help", is_args=False)
@peru_only
async def deepislub(event):
    grabonx = "Hello Here Are Some Commands \n➤ /start - Check if I am Alive \n➤ /ping - Pong! \n➤ /tr <lang-code> \n➤ /broadcast - Sends Message To all Users In Bot \n➤ /id - Shows ID of User And Media. \n➤ /addnote - Add Note \n➤ /notes - Shows Notes \n➤ /rmnote - Remove Note \n➤ /alive - Am I Alive? \n➤ /bun - Works In Group , Bans A User. \n➤ /unbun - Unbans A User in Group \n➤ /prumote - Promotes A User \n➤ /demute - Demotes A User \n➤ /pin - Pins A Message \n➤ /stats - Shows Total Users In Bot"
    await event.reply(grabonx)


@admin_cmd("block", is_args=False)
@god_only
async def deepvirk(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@admin_cmd("unblock", is_args=False)
@god_only
async def deepvirk(event):
    if event.sender_id == bot.uid:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even. Blacklisted 🤦🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await tgbot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )
