import logging
from pathlib import Path
from sys import argv
import var
import telethon.utils
from telethon import TelegramClient
from telethon import events,Button
import os
from var import Var
from . import beast  
from telethon.tl import functions
from beastx.Configs import Config
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import InputMessagesFilterDocument

from resources.startup.sanskar import autobot,autopilot,customize
from beastx.utils import load_module, start_assistant
import asyncio
from telethon.tl.functions.channels import InviteToChannelRequest
from . import bot
bot = beast
sed = logging.getLogger("beastx")

#rom . import semxx,semxxx
#####################################
plugin_channel = "@BeastX_Plugins" 
#####################################
if Var.TG_BOT_TOKEN_BF_HER is None:
    try:
        print("BOT_TOKEN not Found")
        bot.loop.run_until_complete(autobot())
    except BaseException as er:
        print(er)
else:
    pass




sur = Config.PRIVATE_GROUP_ID

UL = Config.TG_BOT_USER_NAME_BF_HER

VR = "Beast 0.1"
chat_id = sur




sed = logging.getLogger("beastx")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)
   
    #om = await beast.get_me()

    #mm = await sedmrunal.get_me()
    #try:
        #MSG = f"""

#✨𝔹𝕖𝕒𝕤𝕥 ℍ𝕒𝕤 𝔹𝕖𝕖𝕟 𝔻𝕖𝕡𝕝𝕠𝕪𝕖𝕕!

 #---------------------
#┏━━━━━━━━━━━━━━━━━
#┣•Assistant➠ @{mm.username}
#┣•User➠ @{om.username}
#┣•Version➠ {VR}
#┗━━━━━━━━━━━━━━━━━

#Do `.ping `or` /alive` for check userbot working

#"""
'''
        await sedmrunal.send_message(sur, MSG,
                                 
                                  buttons=[

                        [Button.url("⭐Updates", url="https://t.me/BeastX_Userbot")],

                        [ Button.url("⚡Support",url="https://t.me/BeastX_Support")]

                    ])
    except Exception as e:
        sed.info(str(e))
        sed.info("---------------------------------------")
        sed.info("Bruh you forgot add assistant in log group")
        sed.info("---------------------------------------")
        '''


try:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()
except BaseException as er:
    sed.info(er)
    
async def a():

  sed.info("Connecting...") ; 

  o = ""

  la = 0

  try:

     await bot.start() ; sed.info("beastx connected") ; o = "client"

  except:

    sed.info("Telegram String Session Wrong or Expired Please Add new one ") ; quit(1)
import glob
async def a():
            documentss = await bot.get_messages(plugin_channel, None , filter=InputMessagesFilterDocument)
            total = int(documentss.total)
            total_doxx = range(0, total)
            for ixo in total_doxx:
                mxo = documentss[ixo].id
                downloaded_file_name = await bot.download_media(await bot.get_messages(chat, ids=mxo), "beastx/modules/")
                if "(" not in downloaded_file_name:
                     path1 = Path(downloaded_file_name)
                     shortname = path1.stem
                     load_module(shortname.replace(".py", ""))
                     sed.info("Installed Plugin `{}` successfully.".format(os.path.basename(downloaded_file_name)))
                else:
                     sed.info("Plugin `{}` has been pre-installed and cannot be installed.".format(os.path.basename(downloaded_file_name)))
           
logger_group = Var.PRIVATE_GROUP_ID
if not str(logger_group).startswith("-100"):
    try:
        bot.loop.run_until_complete(autopilot())
    except BaseException as er:
        print(er)        
else:
    pass
    
bot.loop.run_until_complete(a())

path = "beastx/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


        
if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "beastx/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))
    sed.info("beastx And Assistant Bot Have Been Installed Successfully !")
    sed.info("---------------------------------------")
    sed.info("------------@BeastX_Userbot------------")
    sed.info("---------------------------------------")
         
else:
    sed.info("beastx Has Been Installed Sucessfully !")
    sed.info("Hope you will enjoy")
    



 #await bot.send_message(chat_id,MSG)
    
#else:
   # sed.info("your Get_Msg disable")
    
bot.run_until_disconnected()
