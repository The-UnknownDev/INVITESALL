import os
import sys
import random
import asyncio
import time

from datetime import datetime
from os import execl


from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import  
from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_ID2, API_ID3, API_ID4, API_ID5, API_ID6, API_ID7, API_ID8, API_ID9, API_ID10, API_ID11, API_ID12, API_ID13, API_ID14, API_ID15, API_ID16, API_ID17, API_ID18, API_ID19, API_ID20, API_ID21, API_ID22, API_ID23, API_ID24, API_ID25, API_HASH, API_HASH2, API_HASH3, API_HASH4, API_HASH5, API_HASH6, API_HASH7, API_HASH8, API_HASH9, API_HASH10, API_HASH11, API_HASH12, API_HASH13, API_HASH14, API_HASH15, API_HASH16, API_HASH17, API_HASH18, API_HASH19, API_HASH20, API_HASH21, API_HASH22, API_HASH23, API_HASH24, API_HASH25, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest


from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)

from telethon.tl.functions.channels import GetFullChannelRequest, InviteToChannelRequest    


a = API_ID
2a = API_ID2
3a = API_ID3
4a = API_ID4
5a = API_ID5
6a = API_ID6
7a = API_ID7
8a = API_ID8
9a = API_ID9
10a = API_ID10
11a = API_ID11
12a = API_ID12
13a = API_ID13
14a = API_ID14
15a = API_ID15
16a = API_ID16
17a = API_ID17
18a = API_ID18
19a = API_ID19
20a = API_ID20
21a = API_ID21
22a = API_ID22
23a = API_ID23
24a = API_ID24
25a = API_ID25

b = API_HASH
2b = API_HASH2
3b = API_HASH3
4b = API_HASH4
5b = API_HASH5
6b = API_HASH6
7b = API_HASH7
8b = API_HASH8
9b = API_HASH9
10b = API_HASH10
11b = API_HASH11
12b = API_HASH12
13b = API_HASH13
14b = API_HASH14
15b = API_HASH15
16b = API_HASH16
17b = API_HASH17
18b = API_HASH18
19b = API_HASH19
20b = API_HASH20
21b = API_HASH21
22b = API_HASH22
23b = API_HASH23
24b = API_HASH24
25b = API_HASH25

smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING10
eleve = STRING11
twelv = STRING12
thirt = STRING13
forte = STRING14
fifth = STRING15
sieee = STRING16
seeee = STRING17
eieee = STRING18
nieee = STRING19
gandu = STRING20
ekish = STRING21
baish = STRING22
teish = STRING23
tfour = STRING24
tfive = STRING25


idk = ""
ydk = ""
wdk = ""
sdk = ""
hdk = ""
adk = ""
bdk = ""
cdk = ""
edk = ""
ddk = ""
vkk = ""
kkk = ""
lkk = ""
mkk = ""
sid = ""
shy = ""
aan = ""
ake = ""
eel = ""
khu = ""
shi = ""
yaa = ""
dav = ""
raj = ""
put = ""


que = {}

SMEX_USERS = []
for x in SUDO: 
    SMEX_USERS.append(x)
    
async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put
    
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), api_id=a, api_hash=b, connection=ConnectionTcpAbridged, auto_reconnect=True, connection_retries=None)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await idk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await idk(functions.channels.JoinChannelRequest(channel="@LegendFonts"))
            await idk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), 1a, 1b)
        try:
            print("Booting Up The Client 2")
            await ydk.start()
            await ydk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await ydk(functions.channels.JoinChannelRequest(channel="@Its_LegendBot_BOT"))
            await ydk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        ydk = TelegramClient(session_name, 1a, 1b)
        try:
            await ydk.start()
        except Exception as e:
            pass

    if smexxx:
        session_name = str(smexxx)
        print("String 3 Found")
        wdk = TelegramClient(StringSession(session_name), 2a, 2b)
        try:
            print("Booting Up The Client 3")
            await  wdk.start()
            await wdk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await wdk(functions.channels.JoinChannelRequest(channel="@Its_LegendBot_BOT"))
            await wdk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        wdk = TelegramClient(session_name, 3a, 3b)
        try:
            await wdk.start()
        except Exception as e:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), 4a, 4b)
        try:
            print("Booting Up The Client 4")
            await hdk.start()
            await hdk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await hdk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await hdk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        hdk = TelegramClient(session_name, 4a, 4b)
        try:
            await hdk.start()
        except Exception as e:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), 5a, 5b)
        try:
            print("Booting Up The Client 5")
            await sdk.start()
            await sdk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await sdk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await sdk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sdk = TelegramClient(session_name, 6a, 6b)
        try:
            await sdk.start()
        except Exception as e:
            pass
                  
    if sixth:
        session_name = str(sixth)
        print("String 6 Found")
        adk = TelegramClient(StringSession(session_name), 7a, 7b)
        try:
            print("Booting Up The Client 6")
            await adk.start()
            await adk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await adk(functions.channels.JoinChannelRequest(channel="@Offcial_LegendBot"))
            await adk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await adk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        adk = TelegramClient(session_name, 7a, 7b)
        try:
            await adk.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), 8a, 8b)
        try:
            print("Booting Up The Client 7")
            await bdk.start()
            await bdk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await bdk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await bdk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        bdk = TelegramClient(session_name, 8a, 8b)
        try:
            await bdk.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), 8a, 8b)
        try:
            print("Booting Up The Client 8")
            await cdk.start()
            await cdk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await cdk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await cdk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        cdk = TelegramClient(session_name, 8a, 8b)
        try:
            await cdk.start()
        except Exception as e:
            pass   
        
    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), 9a, 9b)
        try:
            print("Booting Up The Client 9")
            await ddk.start()
            await ddk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await ddk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await ddk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        ddk = TelegramClient(session_name, 9a, 9b)
        try:
            await ddk.start()
        except Exception as e:
            pass   
    
  
    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), 10a, 10b)
        try:
            print("Booting Up The Client 10")
            await edk.start()
            await edk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await edk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await edk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await edk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        edk = TelegramClient(session_name, 10a, 10b)
        try:
            await edk.start()
        except Exception as e:
            pass 
        
    
    if eleve:
        session_name = str(eleve)
        print("String 11 Found")
        vkk = TelegramClient(StringSession(session_name), 11a, 11b)
        try:
            print("Booting Up The Client 11")
            await vkk.start()
            await vkk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            await vkk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await vkk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            botme = await vkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "startup"
        vkk = TelegramClient(session_name, 11a, 11b)
        try:
            await vkk.start()
        except Exception as e:
            pass
        
    
    if twelv:
        session_name = str(twelv)
        print("String 12 Found")
        kkk = TelegramClient(StringSession(session_name), 12a, 13b)
        try:
            print("Booting Up The Client 12")
            await kkk.start()
            await kkk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await kkk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await kkk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botme = await kkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "startup"
        kkk = TelegramClient(session_name, 12a, 12b)
        try:
            await kkk.start()
        except Exception as e:
            pass   
    
  
    if thirt:
        session_name = str(thirt)
        print("String 13  Found")
        lkk = TelegramClient(StringSession(session_name), 13a, 13b)
        try:
            print("Booting Up The Client 13")
            await lkk.start()
            await lkk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await lkk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await lkk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botme = await lkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "startup"
        lkk = TelegramClient(session_name, 13a, 13b)
        try:
            await lkk.start()
        except Exception as e:
            pass 
        
    
    if forte:
        session_name = str(forte)
        print("String 14 Found")
        mkk = TelegramClient(StringSession(session_name), 14a, 14b)
        try:
            print("Booting Up The Client 14")
            await mkk.start()
            await mkk(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await mkk(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await mkk(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botme = await mkk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "startup"
        mkk = TelegramClient(session_name, 14a, 14b)
        try:
            await mkk.start()
        except Exception as e:
            pass
        
    
    if fifth:
        session_name = str(fifth)
        print("String 15 Found")
        sid = TelegramClient(StringSession(session_name), 15a, 15b)
        try:
            print("Booting Up The Client 15")
            await sid.start()
            await sid(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await sid(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await sid(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await sid(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botme = await sid.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "startup"
        sid = TelegramClient(session_name, 15a, 15b)
        try:
            await sid.start()
        except Exception as e:
            pass


    if sieee:
        session_name = str(sieee)
        print("String 16 Found")
        shy = TelegramClient(StringSession(session_name), 16a, 16b)
        try:
            print("Booting Up The Client 16")
            await shy.start()
            botme = await shy.get_me()
            await shy(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await shy(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await shy(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await shy(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        shy = TelegramClient(session_name, 16a, 16b)
        try:
            await shy.start()
        except Exception as e:
            pass
   
    if seeee:
        session_name = str(seeee)
        print("String 17 Found")
        aan = TelegramClient(StringSession(session_name), 17a, 17b)
        try:
            print("Booting Up The Client 17")
            await aam.start()
            botme = await aan.get_me()
            await aan(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await aan(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await aan(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await aan(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        aan = TelegramClient(session_name, 17a, 17b)
        try:
            await aan.start()
        except Exception as e:
            pass
   
    if eieee:
        session_name = str(eieee)
        print("String 18 Found")
        ake = TelegramClient(StringSession(session_name), 18a, 18b)
        try:
            print("Booting Up The Client 18")
            await ake.start()
            botme = await ake.get_me()
            await ake(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await ake(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await ake(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await ake(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        ake = TelegramClient(session_name, 18a, 18b)
        try:
            await ake.start()
        except Exception as e:
            pass
   
    if nieee:
        session_name = str(nieee)
        print("String 19 Found")
        eel = TelegramClient(StringSession(session_name), 19a, 19b)
        try:
            print("Booting Up The Client 19")
            await eel.start()
            botme = await eel.get_me()
            await eel(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await eel(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await eel(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await eel(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        eel = TelegramClient(session_name, 19a, 19b)
        try:
            await idk.start()
        except Exception as e:
            pass
   
    if gandu:
        session_name = str(gandu)
        print("String 20 Found")
        khu = TelegramClient(StringSession(session_name), 20a, 20b)
        try:
            print("Booting Up The Client 20")
            await khu.start()
            botme = await khu.get_me()
            await khu(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await khu(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await khu(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await khu(functions.channels.JoinChannelRequest(channel="@Official__LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        khu = TelegramClient(session_name, 20a, 20b)
        try:
            await khu.start()
        except Exception as e:
            pass
   
    if ekish:
        session_name = str(ekish)
        print("String 21 Found")
        shi = TelegramClient(StringSession(session_name), 21a, 21b)
        try:
            print("Booting Up The Client 21")
            await shi.start()
            botme = await shi.get_me()
            await shi(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await shi(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await shi(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await shi(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        shi = TelegramClient(session_name, 21a, 21b)
        try:
            await shi.start()
        except Exception as e:
            pass
   
    if baish:
        session_name = str(baish)
        print("String 22 Found")
        yaa = TelegramClient(StringSession(session_name), 22a, 22b)
        try:
            print("Booting Up The Client 22")
            await yaa.start()
            botme = await yaa.get_me()
            await yaa(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await yaa(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await yaa(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        yaa = TelegramClient(session_name, 22a, 22b)
        try:
            await yaa.start()
        except Exception as e:
            pass
   
    if teish:
        session_name = str(teish)
        print("String 23 Found")
        dav = TelegramClient(StringSession(session_name), 23a, 23b)
        try:
            print("Booting Up The Client 23")
            await dav.start()
            botme = await dav.get_me()
            await dav(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await dav(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await dav(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await dav(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        dav = TelegramClient(session_name, 23a, 23b)
        try:
            await dav.start()
        except Exception as e:
            pass
   
    if tfour:
        session_name = str(tfour)
        print("String 24 Found")
        raj = TelegramClient(StringSession(session_name), 24a, 24b)
        try:
            print("Booting Up The Client 24")
            await raj.start()
            botme = await raj.get_me()
            await raj(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await raj(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await raj(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await raj(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        raj = TelegramClient(session_name, 24a, 24b)
        try:
            await raj.start()
        except Exception as e:
            pass
   
    if tfive:
        session_name = str(tfive)
        print("String 25 Found")
        put = TelegramClient(StringSession(session_name), 25a, 25b)
        try:
            print("Booting Up The Client 25")
            await put.start()
            botme = await put.get_me()
            await put(functions.channels.JoinChannelRequest(channel="@Legend_Userbot"))
            await put(functions.channels.JoinChannelRequest(channel="@LEGEND_MR_LOGOS"))
            await put(functions.channels.JoinChannelRequest(channel="@Legend_UserbotSpam"))
            await put(functions.channels.JoinChannelRequest(channel="@Official_LegendBot"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        put = TelegramClient(session_name, a, b)
        try:
            await put.start()
        except Exception as e:
            pass
   
   
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())       

async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass

def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


async def get_chatinfo(event):
    yukki = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    chat = yukki[0]
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.edit("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.edit(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.join")) 
@sid.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.join"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝐉𝐎𝐢𝐍 𝐇𝐎𝐆𝐘𝐀 𝐕𝐀𝐈 AB BATA KISKO MARU PAHLE🔥")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pjoin")) 
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("𝐉𝐎𝐢𝐍 𝐇𝐎𝐆𝐘𝐀 𝐕𝐀𝐈 𝐀𝐁 𝐁𝐓𝐀 𝐊𝐈𝐒𝐊𝐈 𝐌𝐀𝐑𝐔😏🔥")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@idk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.pleave"))

async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) == 7:
            bc = yukki[0]
            bc = int(bc)
            text = "BOT Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
           
       

@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"PING PONG!\n`{ms}` 𝗺𝘀")



@idk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.invitesall"))
async def get_users(event):
    legen_ = event.text[11:]
    legend_chat = legen_.lower
    restricted = ["@Legend_Userbot", "@Official_LegendBot"]
    legend = await eor(event, f"**Inviting members from** {legen_}")
    if legend_chat in restricted:
        await event.edit("You can't Invite Members from there.")
        await bot.send_message(-1001344140905, "Sorry for inviting members from here.")
        return
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        text = "Processing...."
        krishna = await event.reply(text, parse_mode=None, link_preview=None )
    else:
        text = "Processing...."
        krishna = await event.reply(text, parse_mode=None, link_preview=None )...`")
    legend = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await krishna.edit("`Sorry, Cant add users here`")
    s = 0
    f = 0
    error = "None"

    await krishna.edit(
        "**⚜️[Ͳєямιиαℓ Տτατυѕ](https://t.me/Legend_Userbot)**\n\n`🔸Inviting Users.......`"
    )
    async for user in event.client.iter_participants(legend.full_chat.id):
        try:
            await bot(InviteToChannelRequest(channel=chat, users=[user.id]))
            s = s + 1
            await krishna.edit(
                f"🤟**Inviting Users👇 **\n\n**⚜Invited :**  `{s}` users \n**🔰Failed to Invite :**  `{f}` users.\n\n**×Error :**  `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await krishna.edit(
        f"[τєямנиαℓ ƒιиιѕнє∂](https://t.me/Legend_Userbot) \n\n🔸 Sυϲϲєѕѕƒυℓℓγ ιиνιτє∂ `{s}` ρєορℓє \n⚠️ ƒαιℓє∂ το ιиνιτє `{f}` ρєορℓє"
    )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.inviteall"))
async def get_users(event):
    if event.sender_id in SMEX_USERS: 
        sender = await event.get_sender()
        me = await event.client.get_me()
        if not sender.id == me.id:
            text = "Processing...."
            krishna = await event.reply(text, parse_mode=None, link_preview=None )
        else:
            text = "processing.."
            krishna = await event.reply(text, parse_mode=None, link_preview=None )
        aura = await get_chatinfo(event)
        chat = await event.get_chat()
        if event.is_private:
            return await krishna.edit("`Sorry, Cant add users here`")
        s = 0
        f = 0
        error = "None"
        await krishna.edit("**TerminalStatus**\n\n`Collecting Users.......`")
        async for user in event.client.iter_participants(aura.full_chat.id):
            try:
                if error.startswith("Too"):
                    return await krishna.edit(
                        f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people"
                    )
                await event.client(
                    functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
                )
                s = s + 1
                await krishna.edit(
                    f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`"
                )
            except Exception as k:
                error = str(k)
                f = f + 1
            await krishna.edit(
                f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people"
            )
            await asyncio.sleep(300)
            await krishna.delete()

@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ydk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@wdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@hdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@adk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@cdk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@edk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ddk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@vkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@kkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@lkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@mkk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@sid.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shy.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@aan.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ake.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@eel.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@khu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@shi.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@yaa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@dav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@raj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@put.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await idk.disconnect()
        except Exception as e:
            pass
        try:
            await ydk.disconnect()
        except Exception as e:
            pass
        try:
            await wdk.disconnect()
        except Exception as e:
            pass
        try:
            await hdk.disconnect()
        except Exception as e:
            pass
        try:
            await sdk.disconnect()
        except Exception as e:
            pass
        try:
            await adk.disconnect()
        except Exception as e:
            pass
        try:
            await bdk.disconnect()
        except Exception as e:
            pass
        try:
            await cdk.disconnect()
        except Exception as e:
            pass
        try:
            await ddk.disconnect()
        except Exception as e:
            pass
        try:
            await edk.disconnect()
        except Exception as e:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()        

    
        
text = """
CONGRATS🥳🥳🥳 YOUR FASTEST, SMOOTHEST AND POWERFUL LEGENDSPAMBOT DEPLOYED SUCCESSFULLY """

print(text)
print("")
print("🙏🔥🔥YOUR! LEGEND SPAM BOT STARTED SUCCESFULLY.🔥🔥🙏")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception as e:
        pass
    try:
        ydk.disconnect()
    except Exception as e:
        pass
    try:
        wdk.disconnect()
    except Exception as e:
        pass
    try:
        hdk.disconnect()
    except Exception as e:
        pass
    try:
        sdk.disconnect()
    except Exception as e:
        pass
    try:
        adk.disconnect()
    except Exception as e:
        pass
    try:
        bdk.disconnect()
    except Exception as e:
        pass
    try:
        cdk.disconnect()
    except Exception as e:
        pass
    try:
        edk.disconnect()
    except Exception as e:
        pass
    try:
        ddk.disconnect()
    except Exception as e:
        pass
    try:
        vkk.disconnect()
    except Exception as e:
        pass 
    try:
        kkk.disconnect()
    except Exception as e:
        pass
    try:
        lkk.disconnect()
    except Exception as e:
        pass 
    try:
        mkk.disconnect()
    except Exception as e:
        pass
    try:
        sid.disconnect()
    except Exception as e:
        pass
    try:
        shy.disconnect()
    except Exception as e:
        pass
    try:
        aan.disconnect()
    except Exception as e:
        pass
    try:
        ake.disconnect()
    except Exception as e:
        pass
    try:
        eel.disconnect()
    except Exception as e:
        pass
    try:
        khu.disconnect()
    except Exception as e:
        pass
    try:
        shi.disconnect()
    except Exception as e:
        pass
    try:
        yaa.disconnect()
    except Exception as e:
        pass
    try:
        dav.disconnect()
    except Exception as e:
        pass
    try:
        raj.disconnect()
    except Exception as e:
        pass
    try:
        put.disconnect()
    except Exception as e:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        adk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        edk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sid.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shy.run_until_disconnected()
    except Exception as e:
        pass
    try:
        aan.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ake.run_until_disconnected()
    except Exception as e:
        pass
    try:
        eel.run_until_disconnected()
    except Exception as e:
        pass
    try:
        khu.run_until_disconnected()
    except Exception as e:
        pass
    try:
        shi.run_until_disconnected()
    except Exception as e:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        dav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        raj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        put.run_until_disconnected()
    except Exception as e:
        pass
