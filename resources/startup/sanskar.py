import asyncio
import os
import time
from random import randint
from urllib.request import urlretrieve
import heroku3
from pytz import timezone
from telethon.errors.rpcerrorlist import ChannelsTooMuchError
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    JoinChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatAdminRights,
    InputChatUploadedPhoto,
    InputMessagesFilterDocument,
)

from beastx import Var
HEROKU_APP_NAME = Var.HEROKU_APP_NAME
HEROKU_API_KEY = Var.HEROKU_API_KEY
heroku = heroku3.from_key(HEROKU_API_KEY)
app = heroku.apps()[HEROKU_APP_NAME]
heroku_var = app.config()





async def download_file(link, name):
    """for files, without progress callback with aiohttp"""
    if not aiohttp:
        urllib.request.urlretrieve(link, name)
        return name
    async with aiohttp.ClientSession() as ses:
        async with ses.get(link) as re_ses:
            file = await aiofiles.open(name, "wb")
            await file.write(await re_ses.read())
            await file.close()
    return name

async def autobot():
    from beastx import beast
    if Var.TG_BOT_TOKEN_BF_HER is not None:
        print("BOT_TOKEN Found")
    else:
        await beast.start()
        print("MAKING A TELEGRAM BOT FOR YOU AT @BotFather, Kindly Wait")
    who = beast.me
    name = who.first_name + "'s Assistant Bot"
    if who.username:
        username = who.username + "_bot"
    else:
        username = "Beast_" + (str(who.id))[5:] + "_bot"
    bf = "@BotFather"
    await beast(UnblockRequest(bf))
    await beast.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await beast.send_message(bf, "/start")
    await asyncio.sleep(1)
    await beast.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await beast.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        print(
            "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
        )
        exit(1)
    await beast.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await beast.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await beast.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await beast.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
            )
            exit(1)
    await beast.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await beast.get_messages(bf, limit=1))[0].text
    await beast.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "Beast_" + (str(who.id))[6:] + str(ran) + "_bot"
        await beast.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await beast.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            heroku_var['TG_BOT_TOKEN_BF_HER'] = token
            await beast.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await beast.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await beast.send_message(bf, "Search")
            print(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
        else:
            print(
                "Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
            )

            exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        heroku_var['TG_BOT_TOKEN_BF_HER'] = token
        await beast.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await beast.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await beast.send_message(bf, "Search")
        print(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
    else:
        print(
            "Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
        )

        exit(1)
async def autopilot():
    from beastx import tgbot,beast

    if Var.PRIVATE_GROUP_ID and str(Var.PRIVATE_GROUP_ID).startswith("-100"):
        try:
            await beast.get_entity(int(Var.PRIVATE_GROUP_ID))
            return
        except BaseException as er:
            LOGS.error(er)
            del heroku_var['PRIVATE_GROUP_ID']
    print("Creating a Log Channel for You!")
    try:
        r = await beast(
            CreateChannelRequest(
                title="My BeastX Logs",
                about="My BeastX Log Group\n\n Join @BeastX_Userbot",
                megagroup=True,
            ),
        )
    except ChannelsTooMuchError:
        print(
            "You Are in Too Many Channels & Groups , Leave some And Restart The Bot"
        )
        exit(1)
    except BaseException as er:
        print(er)
        print(
            "Something Went Wrong , Create A Group and set its id on config var LOG_CHANNEL."
        )
        exit(1)
    chat = r.chats[0]
    chat_id = chat.id
    if not str(chat_id).startswith("-100"):
        heroku_var['PRIVATE_GROUP_ID'] = "-100" + str(chat_id)
    else:
        heroku_var['PRIVATE_GROUP_ID'] = str(chat_id)
    rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        anonymous=False,
        manage_call=True,
    )
    await beast(EditAdminRequest(chat_id, tgbot.me.username, rights, "Assistant"))
    photo = await download_file(
        "https://telegra.ph/file/4a1e0ee716f805cf66777.jpg", "channelphoto.jpg"
    )
    ll = await beast.upload_file(photo)
    await beast(EditPhotoRequest(chat_id, InputChatUploadedPhoto(ll)))
    os.remove(photo)


# customize assistant


async def customize():
    from beastx import tgbot,beast

    try:
        chat_id = Var.PRIVATE_GROUP_ID
        if tgbot.me.photo:
            return
        print("Customising Ur Assistant Bot in @BOTFATHER")
        UL = f"@{tgbot.me.username}"
        if (beast.me.username) is None:
            sir = beast.me.first_name
        else:
            sir = f"@{beast.me.username}"
        await beast.send_message(
            chat_id, "Auto Customisation Started on @botfather"
        )
        await asyncio.sleep(1)
        await beast.send_message("botfather", "/cancel")
        await asyncio.sleep(1)
        await beast.send_message("botfather", "/start")
        await asyncio.sleep(1)
        await beast.send_message("botfather", "/setuserpic")
        await asyncio.sleep(1)
        await beast.send_message("botfather", UL)
        await asyncio.sleep(1)
        await beast.send_file(
            "botfather", "resources/beastxthumb.jpg"
        )
        await asyncio.sleep(2)
        await beast.send_message("botfather", "/setabouttext")
        await asyncio.sleep(1)
        await beast.send_message("botfather", UL)
        await asyncio.sleep(1)
        await beast.send_message(
            "botfather", f"✨ Hello ✨!! I'm Assistant Bot of {sir}"
        )
        await asyncio.sleep(2)
        await beast.send_message("botfather", "/setdescription")
        await asyncio.sleep(1)
        await beast.send_message("botfather", UL)
        await asyncio.sleep(1)
        await beast.send_message(
            "botfather",
            f"✨ PowerFul BeastX Assistant Bot ✨\n✨ Master ~ {sir} ✨\n\n✨ Powered By ~ @TeamBeastX ✨",
        )
        await asyncio.sleep(2)
        await beast.send_message(
            chat_id, "**Auto Customisation** Done at @BotFather"
        )
        print("Customisation Done")
    except Exception as e:
        print.exception(e)
