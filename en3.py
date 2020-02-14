# -*- coding: utf-8 -*-
from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit
#-------------------------------------------------------------------------------
botStart = time.time()
#-------------------------------------------------------------------------------
gye = LINE() #[Bot1]/name gye#
gye.log("Auth Token : " + str(gye.authToken))
channelToken = gye.getChannelResult()
gye.log("Channel Token : " + str(channelToken))
#-------------------------------------------------------------------------------
ais = LINE() #[Bot2]/name ais#
ais.log("Auth Token : " + str(ais.authToken))
channelToken = ais.getChannelResult()
ais.log("Channel Token : " + str(channelToken))
#-------------------------------------------------------------------------------
ki2 = LINE() #[Bot3]/name ki2#
ki2.log("Auth Token : " + str(ki2.authToken))
channelToken = ki2.getChannelResult()
ki2.log("Channel Token : " + str(channelToken))
#-------------------------------------------------------------------------------
KAC = [gye,ais,ki2]
GUE = [ais,ki2] 
#-------------------------------------------------------------------------------
gyeMID = gye.profile.mid
aisMID = ais.profile.mid
ki2MID = ki2.profile.mid
#-------------------------------------------------------------------------------
Bots = ["u78d3b315b4268d7b3654f8486e07e5e0","u7b4abcec38a39e8ab52b0c939eb79fa9","u3bc28db881a917b7e8add49a47e6df72"]
creator = ["u78d3b315b4268d7b3654f8486e07e5e0"]
Owner = ["u78d3b315b4268d7b3654f8486e07e5e0"]
admin = ["u78d3b315b4268d7b3654f8486e07e5e0"]
#-------------------------------------------------------------------------------
gyeProfile = gye.getProfile()
aisProfile = ais.getProfile()
ki2Profile = ki2.getProfile()
#-------------------------------------------------------------------------------
lineSettings = gye.getSettings()
aisSettings = ais.getSettings()
ki2Settings = ki2.getSettings()
#-------------------------------------------------------------------------------
oepoll = OEPoll(gye)
oepoll1 = OEPoll(ais)
oepoll2 = OEPoll(ki2)
#-------------------------------------------------------------------------------
responsename = gye.getProfile().displayName
responsename2 = ais.getProfile().displayName
responsename3 = ki2.getProfile().displayName
#-------------------------------------------------------------------------------
with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
#-------------------------------------------------------------------------------    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
#-------------------------------------------------------------------------------    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
settings = {
   "blacklist":{},
   "dblacklist": False,
   "wblacklist": False,
   "winvite": False,
}
#-------------------------------------------------------------------------------
myProfile["displayName"] = gyeProfile.displayName
myProfile["statusMessage"] = gyeProfile.statusMessage
myProfile["pictureStatus"] = gyeProfile.pictureStatus
#-------------------------------------------------------------------------------
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
#-------------------------------------------------------------------------------
read = json.load(readOpen)
settings = json.load(settingsOpen)
#-------------------------------------------------------------------------------
def restartBot():
    print ("[ INFO ] BOT R E S T A R T ")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#-------------------------------------------------------------------------------   
def logError(text):
    gye.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#-------------------------------------------------------------------------------       
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        gye.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
#-------------------------------------------------------------------------------       
def helpmessage():
    helpMessage = """꧁Bots Prevent By Cola꧂

꧁English Commands꧂

╭═════════════════╮
╠➣ help
╠➣ cola1
╠➣ cola2
╠➣ cola3
╠➣ cola4
╠➣ cola5
╠➣ status
╠➣ bot in
╰═════════════════╯"""
    return helpMessage
#-------------------------------------------------------------------------------    
def helpcola1():
    helpCola1 = """꧁Bot Prevent By Cola꧂

English Commands

꧁on/off Commands꧂

╭═════════════════╮
╠➣ protect「on/off」
╠➣ qrprotect「on/off」
╠➣ inviteprotect「on/off」
╠➣ cancelprotect「on/off」
╠➣ botprotect「on/off」
╠➣ autoadd 「on/off」
╠➣ autojoin「on/off」
╠➣ autoleave「on/off」
╠➣ autoRead「on/off」
╠➣ checksticker「on/off」
╠➣ detectmention「on/off」
╠➣ status
╠➣ qr「on/off」
╠➣ qr = Show qr
╰═════════════════╯
* on = open ✅ off = close ❌ *"""
    return helpCola1
#-------------------------------------------------------------------------------   
def helpcola2():
    helpCola2 = """꧁Bot Prevent By Cola꧂

English Commands

꧁Group Commands꧂

╭═════════════════╮
╠➣ groupcreator
╠➣ groupid
╠➣ groupname
╠➣ grouppicture
╠➣ grouplist
╠➣ groupmemberlist
╠➣ groupInfo
╠➣ qr「on/off」
╠➣ qr
╠➣ tack
╰═════════════════╯"""
    return helpCola2
#-------------------------------------------------------------------------------
def helpcola3():
    helpCola3 = """꧁Bot Prevent By Cola꧂

English Commands

꧁information Commands꧂

╭═════════════════╮
╠➣ me
╠➣ mymid
╠➣ myname
╠➣ mypicture
╠➣ myvideoprofile
╠➣ mybio
╠➣ copycontact @
╠➣ copymid @
╠➣ copyname @
╠➣ copybio @
╠➣ copypicture @
╠➣ copyvideoprofile @
╠➣ copycover @
╠➣ cloneprofile @
╰═════════════════╯"""
    return helpCola3
#-------------------------------------------------------------------------------
def helpcola4():
    helpCola4 = """꧁Bot Prevent By Cola꧂

English Commands

꧁Bot Commands꧂

╭═════════════════╮
╠➣ bot 
╠➣ mymidbot = mid all bot
╠➣ bot in
╠➣ bot go = Bot 2 Bot 3 Exit
╠➣ bot bey = All bots out
╠➣ bot 「on/off」
╠➣ speed bot
╠➣ check bot
╠➣ check bot1
╠➣ check bot2
╠➣ kick @ Kick someone
╠➣ botkick = All kicks
╠➣ flat
╠➣ flatwash
╠➣ botkickflat
╠➣ namebot:
╠➣ biobot:
╠➣ namebot1: Just bot 1
╠➣ biobot1: Just bot 1
╠➣ namebot2: Just bot 2
╠➣ biobot2: Just bot 2
╠➣ namebot3: Just bot 3
╠➣ biobot3: Just bot 3
╰═════════════════╯
*namebot: = Change all name*
Method Print Namebot: Followed by the desired name

*biobot: = Change all statuses*
How to type biobot: Follow with the desired word."""
    return helpCola4
#-------------------------------------------------------------------------------       
def helpcola5():
    helpCola5 = """꧁Bot Prevent By Cola꧂

English Commands

꧁The web Commands꧂

╭═════════════════╮
╠➣ youtube
╠➣ pron
╰═════════════════╯
*youtube*
How to type youtube followed by the search term

*pron*
Submit webpage list"""
    return helpCola5    
#-------------------------------------------------------------------------------
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
#-------------------------------------------------------------------------------      
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        
#-------------------------------------------------------------------------------
def lineBot(op):
    try: 
        if op.type == 0:
            print ("[ 0 ] COLA_BOT_PREVENT")
            return
#-------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        gye.sendMessage(to, "Got it")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        gye.sendMessage(to, "decided not to comment")

               elif settings["dblack"] == True:
                   if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        gye.sendMessage(to, "Removed from banned items")
                        settings["dblack"] = False

                   else:
                        settings["dblack"] = False
                        gye.sendMessage(to, "Nothing blacklisted")
               elif settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        gye.sendMessage(to, "Sudah Ada")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        gye.sendMessage(to, "This account has been added to the black list.")

               elif settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        gye.sendMessage(to, "This account has been added to the white list.")
                        settings["dblacklist"] = False

                   else:
                        settings["dblacklist"] = False
                        gye.sendMessage(to, "This account has been added to the white list.")                                               
#-------------------------------------------------------------------------------
        if op.type == 25:
            print ("[ 25 ] COLA_BOT_PREVENT")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != gye.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#-------------------------------------------------------------------------------
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    gye.sendMessage(to, str(helpMessage))
                    gye.sendMessage(to, "=============================\nCreate By : COLA\nBot Name : BOT COLA\nVersion : Bot 3\nVersion Bot : Prevent\n=============================")
                    sendMessageWithMention(to, gyeMID)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'cola1':
                    helpCola1 = helpcola1()
                    gye.sendMessage(to, str(helpCola1))
                    gye.sendMessage(to, "=============================\nCreate By : COLA\nBot Name : BOT COLA\nVersion : Bot 3\nVersion Bot : Prevent\n=============================")
                    sendMessageWithMention(to, gyeMID)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'cola2':
                    helpCola2 = helpcola2()
                    gye.sendMessage(to, str(helpCola2))
                    gye.sendMessage(to, "=============================\nCreate By : COLA\nBot Name : BOT COLA\nVersion : Bot 3\nVersion Bot : Prevent\n=============================")
                    sendMessageWithMention(to, gyeMID)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'cola3':
                    helpCola3 = helpcola3()
                    gye.sendMessage(to, str(helpCola3))
                    gye.sendMessage(to, "=============================\nCreate By : COLA\nBot Name : BOT COLA\nVersion : Bot 3\nVersion Bot : Prevent\n=============================")
                    sendMessageWithMention(to, gyeMID)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'cola4':
                    helpCola4 = helpcola4()
                    gye.sendMessage(to, str(helpCola4))
                    gye.sendMessage(to, "=============================\nCreate By : COLA\nBot Name : BOT COLA\nVersion : Bot 3\nVersion Bot : Prevent\n=============================")
                    sendMessageWithMention(to, gyeMID)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'cola5':
                    helpCola5 = helpcola5()
                    gye.sendMessage(to, str(helpCola5))
                    gye.sendMessage(to, "=============================\nCreate By : COLA\nBot Name : BOT COLA\nVersion : Bot 3\nVersion Bot : Prevent\n=============================")
                    sendMessageWithMention(to, gyeMID)                    
#-------------------------------------------------------------------------------
                elif text.lower() == 'speed':
                    start = time.time()
                    gye.sendMessage(to, "Bot speed ...")
                    elapsed_time = time.time() - start
                    gye.sendMessage(to,format(str(elapsed_time)))
#-------------------------------------------------------------------------------                    
                elif msg.text == "pron":
                	gye.sendMessage(receiver,">https://www.pornhub.com/\n>https://www.xnxx.com/\n>https://www.xvideos.com/\n>https://www5.javmost.com/")
#-------------------------------------------------------------------------------
                elif text.lower() == 'speed bot':
                    start = time.time()
                    gye.sendMessage(to, "Checking speed")
                    elapsed_time = time.time() - start
                    gye.sendMessage(to, "%sseconds" % (elapsed_time))    
                    ais.sendMessage(to, "%sseconds" % (elapsed_time))    
                    ki2.sendMessage(to, "%sseconds" % (elapsed_time))    
                    gye.sendMessage(to, "Speed ​​check done")
#-------------------------------------------------------------------------------
                elif text.lower() == 'speedbot':
                    start = time.time()
                    ais.sendMessage(to, "Checking speed")
                    elapsed_time = time.time() - start    
                    ais.sendMessage(to, "%sseconds" % (elapsed_time))    
                    ki2.sendMessage(to, "%sseconds" % (elapsed_time))    
                    gye.sendMessage(to, "Check bot finished")
#-------------------------------------------------------------------------------                  
                elif text.lower() == 'restart':    
                    gye.sendMessage(to, "Restarting bot wait ...")
                    time.sleep(5)
                    gye.sendMessage(to, "Restart the bot and log in again.")
                    restartBot()
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'online':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    gye.sendMessage(to, "Online time {}".format(str(runtime)))
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ABISHEK SINGH"
                        creator = gye.getContact(owner)
                        contact = gye.getContact("ua287bd3b899219d0da256ea2a2217521")
                        grouplist = gye.getGroupIdsJoined()
                        contactlist = gye.getAllContactIds()
                        blockedlist = gye.getBlockedContactIds()
                        ret_ = "╭════════╬ 🇹🇭 ╬════════╮\nStatus Bot\n ╰════════╬ 🇹🇭 ╬════════╯\n ╭════════╬ 🇹🇭 ╬════════╮\n"
                        ret_ += "\n╠ akun : {}".format(contact.displayName)
                        ret_ += "\n╠ group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ teman : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blokir : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╰════════╬ 🇹🇭 ╬════════╯\n\nGYEVHA BOTS╭════════╬ 🇹🇭 ╬════════╮\n╰════════╬ 🇹🇭 ╬════════╯"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------
                elif text.lower() == 'status':
                    try:
                        ret_ = "╭═════════════════╮\n║͜͡☆➣ ♥ Status Bot ♥\n╰═════════════════╯\n╭═════════════════╮\n"
                        if settings["protect"] == True: ret_ += "║͜͡☆➣ Protect ✅"
                        else: ret_ += "║͜͡☆➣  Protect ❌"
                        if settings["qrprotect"] == True: ret_ += "\n║͜͡☆➣ Qr Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Qr Protect ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n║͜͡☆➣ Invite Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Invite Protect ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n║͜͡☆➣ Cancel Protect ✅"
                        else: ret_ += "\n║͜͡☆➣ Cancel Protect ❌"
                        if settings["autoAdd"] == True: ret_ += "\n║͜͡☆➣ Auto Add ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n║͜͡☆➣ Auto Join ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n║͜͡☆➣ Auto Leave ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n║͜͡☆➣ Auto Read ✅"
                        else: ret_ += "\n║͜͡☆➣ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n║͜͡☆➣ Check Sticker ✅"
                        else: ret_ += "\n║͜͡☆➣ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n║͜͡☆➣ Detect Mention ✅"
                        else: ret_ += "\n║͜͡☆➣ Detect Mention ❌"
                        ret_ += "\n╰═════════════════╯\n╭═════════════════╮\n║͜͡☆➣ ♥ Status Bot ♥\n╰═════════════════╯"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
#-------------------------------------------------------------------------------                        
                elif msg.text.lower().startswith("spaminvite "):
                    dan = text.split("|")
                    userid = dan[0]
                    namagrup = dan[0]
                    jumlah = int(dan[0])
                    grups = gye.groups
                    tgb = gye.findContactsByUserid(userid)
                    if jumlah <= 10000000:
                        for var in range(0,jumlah):
                            try:
                                gye.createGroup(str(namagrup), [tgb.mid])
                                for i in grups:
                                    grup = gye.getGroup(i)
                                    if grup.name == namagrup:
                                        gye.inviteIntoGroup(grup.id, [tgb.mid])
                                        gye.sendMessage(to, "@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                            except Exception as Nigga:
                                gye.sendMessage(to, str(Nigga))
                                gye.sendMessage(to, "@! kebanyakan njer!!", [sender])
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("owneradd"):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                Owner[target] = True
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nAdd\nExecuted")
                            except:
                                pass
#-------------------------------------------------------------------------------                   
                elif msg.text.lower().startswith("ownerdel"):
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del Owner[target]
                                f=codecs.open('Owner.json','w','utf-8')
                                json.dump(Owner, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Owner ☢-Bot-☢\nRemove\nExecuted")
                            except:
                                pass
#-------------------------------------------------------------------------------
                elif text.lower() == 'ownerlist':
                        if Owner == []:
                            gye.sendMessage(msg.to,"The Ownerlist is empty")
                        else:
                            gye.sendMessage(msg.to,"WAITING..")
                            mc = "╔═══════════════\n╠WAR BOT\n╠══✪〘 Owner List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 ABISHEK 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("adminadd"):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                admin[target] = True
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Admin ☢-Bot-☢\nAdd\nExecuted")
                                break
                            except:
                                gye.sendMessage(msg.to,"Added Target Fail !")
                                break
#-------------------------------------------------------------------------------                    
                elif msg.text.lower().startswith("admindel"):
                        targets = []
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            try:
                                del admin[target]
                                f=codecs.open('admin.json','w','utf-8')
                                json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)
                                gye.sendMessage(msg.to,"Admin ☢-Bot-☢\nRemove\nExecuted")
                                break
                            except:
                                gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
#-------------------------------------------------------------------------------
                elif text.lower() == 'adminlist':
                        if admin == []:
                            gye.sendMessage(msg.to,"The admin list is empty.")
                        else:
                            gye.sendMessage(msg.to,"WAITING..")
                            mc = "╔═══════════════\n╠WAR BOT\n╠══✪〘 Admin List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 Accomplished 〙\n╚═══════════════")
#-------------------------------------------------------------------------------                            
                elif "youtube " in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[Search results]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Amount found {} ]".format(len(datas))
                        gye.sendMessage(to, str(ret_))         
#-------------------------------------------------------------------------------
                elif text.lower() == 'protect on':
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Already on ✅ ")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Set To on ✅")
#-------------------------------------------------------------------------------                               
                elif text.lower() == 'protect off':
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Already ❌ ")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Set To off ❌ ")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'qrprotect on':
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Already on ✅ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To on ✅ ")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To on ✅ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Already on ✅ ")
#-------------------------------------------------------------------------------                                
                elif text.lower() == 'qrprotect off':
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Already off ❌ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To off ❌ ")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Qr Set To off ❌ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Qr Already off ❌ ")
#-------------------------------------------------------------------------------
                elif text.lower() == 'inviteprotect on':
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Already on ✅ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To ✅ ")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To ✅ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Already on ✅ ")
#-------------------------------------------------------------------------------                               
                elif text.lower() == 'inviteprotect off':
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Invite Protect off ❌ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Invite Protect off ❌ ")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Invite Protect off ❌ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Invite Protect off ❌ ")
#-------------------------------------------------------------------------------
                elif text.lower() == 'cancelprotect on':
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Already on ✅ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To on ✅ ")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Set To on ✅ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Invite Already on ✅ ")
#-------------------------------------------------------------------------------                                
                elif text.lower() == 'cancelprotect off':
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Invite Already off ❌ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To off ❌ ")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Set To off ❌ ")
                            else:
                                gye.sendMessage(msg.to,"➲ Protection Cancel Invite Already off ❌ ")
#-------------------------------------------------------------------------------
                elif text.lower() == 'bot on':
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        gye.sendMessage(msg.to,"protect on")
                        gye.sendMessage(msg.to,"qr protect on")
                        gye.sendMessage(msg.to,"invite protect on")
                        gye.sendMessage(msg.to,"cancel protect on")
                        gye.sendMessage(msg.to,"➲ Total protect on!")
#-------------------------------------------------------------------------------                       		            
                elif text.lower() == 'bot off':
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        gye.sendMessage(msg.to,"protect off")
                        gye.sendMessage(msg.to,"qr protect off")
                        gye.sendMessage(msg.to,"invite protect off")
                        gye.sendMessage(msg.to,"cancel protect off")
                        gye.sendMessage(msg.to,"➲ Total protect off!")
#-------------------------------------------------------------------------------
                elif text.lower() == 'autoadd on':
                    settings["autoAdd"] = True
                    gye.sendMessage(to, "➲ Successfully enabled auto add.")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'autoadd off':
                    settings["autoAdd"] = False
                    gye.sendMessage(to, "➲ Successfully disabled auto add.")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'autojoin on':    
                    settings["autoJoin"] = True
                    gye.sendMessage(to, "➲ Successfully enabled auto attendant.")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'autojoin off':   
                    settings["autoJoin"] = False
                    gye.sendMessage(to, "➲ Successfully disabling auto attendant")
#-------------------------------------------------------------------------------                   
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    gye.sendMessage(to, "➲ Successfully activated Auto Leave")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    gye.sendMessage(to, "➲ Successfully disabled Auto Leave")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    gye.sendMessage(to, "➲ Successfully activated Auto Read")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    gye.sendMessage(to, "➲ Successfully deactivated Auto Read")
#-------------------------------------------------------------------------------                   
                elif text.lower() == 'checksticker on':
                    settings["checkSticker"] = True
                    gye.sendMessage(to, "➲ Successfully activated the Check Details Sticker")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'checksticker off':
                    settings["checkSticker"] = False
                    gye.sendMessage(to, "➲ Successfully disabled Check Details Sticker")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    gye.sendMessage(to, "➲ Successfully activated Detect Mention")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    gye.sendMessage(to, "➲ Successfully deactivated Detect Mention")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'joinlink on':
                    settings["autoJoinTicket"] = True
                    gye.sendMessage(to, "➲ Successfully activated the Auto Join Link")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'joinlink off':
                    settings["autoJoinTicket"] = False
                    gye.sendMessage(to, "➲ Successfully disabled Auto Join Link")                    
#-------------------------------------------------------------------------------
                elif msg.text.lower() == 'bot':
                        gye.sendContact(to, gyeMID)
                        ais.sendContact(to, aisMID)
                        ki2.sendContact(to, ki2MID)
#-------------------------------------------------------------------------------                       
                elif text.lower() in ["bot go","cola go"]:    
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
#-------------------------------------------------------------------------------                    
                elif text.lower() in ["bot bye"]:    
                    gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
#-------------------------------------------------------------------------------                    
                elif text.lower() in ["bot in","cola in"]:    
                    G = gye.getGroup(msg.to)
                    ginfo = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = False
                    gye.updateGroup(G)
                    invsend = 0
                    Ticket = gye.reissueGroupTicket(msg.to)
                    ais.acceptGroupInvitationByTicket(msg.to,Ticket)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = gye.getGroup(msg.to)
                    G.preventedJoinByTicket = True
                    gye.updateGroup(G)
                    G.preventedJoinByTicket(G)
                    gye.updateGroup(G)
#-------------------------------------------------------------------------------                
                elif text.lower() == 'me':
                    sendMessageWithMention(to, gyeMID)
                    gye.sendContact(to, gyeMID)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'mymid':
                    gye.sendMessage(msg.to,"[MID]\n" +  gyeMID)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'mymidbot':
                    gye.sendMessage(msg.to,"[ MID BOT ¹ ]\n" +  gyeMID)
                    ais.sendMessage(msg.to,"[ MID BOT ² ]\n" +  aisMID)
                    ki2.sendMessage(msg.to,"[ MID BOT ³ ]\n" +  ki2MID)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'myname':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'mybio':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'mypicture':
                    me = gye.getContact(gyeMID)
                    gye.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
#-------------------------------------------------------------------------------                   
                elif text.lower() == 'myvideoprofile':
                    me = gye.getContact(gyeMID)
                    gye.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'mycover':
                    me = gye.getContact(gyeMID)
                    cover = gye.getProfileCoverURL(gyeMID)    
                    gye.sendImageWithURL(msg.to, cover)
#-------------------------------------------------------------------------------                    
                elif msg.text in ["botkickflat"]:
                	if msg.toType == 2:
                         group = gye.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             gye.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[gye]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     gye.sendMessage(receiver,"Nots in Blacklist")
                                     print ("Blacklist di Kick")
#-------------------------------------------------------------------------------
                elif "namebot: " in text.lower():
                    if msg._from in Owner:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = gye.getProfile()
                        profile_B = ais.getProfile()
                        profile_C = ki2.getProfile()
                        profile_A.displayName = string
                        profile_B.displayName = string
                        profile_C.displayName = string
                        gye.updateProfile(profile_A)
                        ais.updateProfile(profile_B)
                        ki2.updateProfile(profile_C)
                        gye.sendMessage(msg.to,"Update Name Bot ¹ to 👉 " + string)
                        ais.sendMessage(msg.to,"Update Name Bot ² to 👉" + string)
                        ki2.sendMessage(msg.to,"Update Name Bot ³ to 👉" + string)
                        print ("Update Name Bot 1")
                        print ("Update Name Bot 2")
                        print ("Update Name Bot 3")
#-------------------------------------------------------------------------------
                elif "biobot: " in msg.text.lower():
                    if msg._from in Owner:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = gye.getProfile()
                        profile_B = ais.getProfile()
                        profile_C = ki2.getProfile()
                        profile_A.statusMessage = string
                        profile_B.statusMessage = string
                        profile_C.statusMessage = string
                        gye.updateProfile(profile_A)
                        ais.updateProfile(profile_B)
                        ki2.updateProfile(profile_C)
                        gye.sendMessage(msg.to,"Update Status Bot ¹ 👉 " + string)
                        ais.sendMessage(msg.to,"Update Status Bot ² 👉 " + string)
                        ki2.sendMessage(msg.to,"Update Status Bot ³ 👉 " + string)
                        print ("Update Status Bot 1")
                        print ("Update Status Bot 2")
                        print ("Update Status Bot 3")            
#-------------------------------------------------------------------------------
                elif "namebot1: " in text.lower():
                    if msg._from in Owner:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = gye.getProfile()
                        profile_A.displayName = string
                        gye.updateProfile(profile_A)
                        gye.sendMessage(msg.to,"Update Name Bot ¹ to 👉 " + string)
                        print ("Update Name Bot 1")
#-------------------------------------------------------------------------------
                elif "biobot1: " in msg.text.lower():
                    if msg._from in Owner:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = gye.getProfile()
                        profile_A.statusMessage = string
                        gye.updateProfile(profile_A)
                        gye.sendMessage(msg.to,"Update Status Bot ¹ 👉 " + string)
                        print ("Update Status Bot 1")
#-------------------------------------------------------------------------------
                elif "namebot2: " in text.lower():
                    if msg._from in Owner:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ais.getProfile()
                        profile_A.displayName = string
                        ais.updateProfile(profile_A)
                        ais.sendMessage(msg.to,"Update Name Bot ² to 👉 " + string)
                        print ("Update Name Bot 2")
#-------------------------------------------------------------------------------
                elif "biobot2: " in msg.text.lower():
                    if msg._from in Owner:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ais.getProfile()
                        profile_A.statusMessage = string
                        ais.updateProfile(profile_A)
                        ais.sendMessage(msg.to,"Update Status Bot ² 👉 " + string)
                        print ("Update Status Bot 2")
#-------------------------------------------------------------------------------
                elif "namebot3: " in text.lower():
                    if msg._from in Owner:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki2.getProfile()
                        profile_A.displayName = string
                        ki2.updateProfile(profile_A)
                        ki2.sendMessage(msg.to,"Update Name Bot ³ to 👉 " + string)
                        print ("Update Name Bot 3")
#-------------------------------------------------------------------------------
                elif "biobot3: " in msg.text.lower():
                    if msg._from in Owner:
                        proses = text.split(":")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki2.getProfile()
                        profile_A.statusMessage = string
                        ki2.updateProfile(profile_A)
                        ki2.sendMessage(msg.to,"Update Status Bot ³ 👉 " + string)
                        print ("Update Status Bot 3")                        
#-------------------------------------------------------------------------------                    
                elif msg.text.lower().startswith("copycontact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            mi_d = contact.mid
                            gye.sendContact(msg.to, mi_d)
#-------------------------------------------------------------------------------                            
                elif msg.text.lower().startswith("copymid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        gye.sendMessage(msg.to, str(ret_))
#-------------------------------------------------------------------------------                        
                elif msg.text.lower().startswith("copyname "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
#-------------------------------------------------------------------------------                            
                elif msg.text.lower().startswith("copybio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = gye.getContact(ls)
                            gye.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
#-------------------------------------------------------------------------------                            
                elif msg.text.lower().startswith("copypicture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus
                            gye.sendImageWithURL(msg.to, str(path))
#-------------------------------------------------------------------------------                            
                elif msg.text.lower().startswith("copyvideoprofile "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.gye.naver.jp/" + gye.getContact(ls).pictureStatus + "/vp"
                            gye.sendImageWithURL(msg.to, str(path))
#-------------------------------------------------------------------------------                            
                elif msg.text.lower().startswith("copycover "):
                    if line != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = gye.getProfileCoverURL(ls)
                                gye.sendImageWithURL(msg.to, str(path))
#-------------------------------------------------------------------------------                                
                elif msg.text.lower().startswith("cloneprofile "):    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            gye.cloneContactProfile(contact)
                            gye.sendMessage(msg.to, "Successful clone members wait a while until the profile changes")
                        except:
                            gye.sendMessage(msg.to, "Failed clone member")
                elif text.lower() == 'restoreprofile':    
                    try:
                        gyeProfile.displayName = str(myProfile["displayName"])
                        gyeProfile.statusMessage = str(myProfile["statusMessage"])
                        gyeProfile.pictureStatus = str(myProfile["pictureStatus"])
                        gye.updateProfileAttribute(8, gyeProfile.pictureStatus)
                        gye.updateProfile(gyeProfile)
                        gye.sendMessage(msg.to, "Successfully restore profile wait a few moments until the profile changes")
                    except:
                        gye.sendMessage(msg.to, "Failed to restore profile")
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            gye.sendMessage(msg.to,"Target added!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Added Target Fail !")
                            break
#-------------------------------------------------------------------------------                            
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            gye.sendMessage(msg.to,"The target has been deleted!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
#-------------------------------------------------------------------------------                            
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        gye.sendMessage(msg.to,"There is no target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+gye.getContact(mi_d).displayName
                        gye.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
#-------------------------------------------------------------------------------                    
                elif "mimic " in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            gye.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            gye.sendMessage(msg.to,"Reply Message off")
#-------------------------------------------------------------------------------
                elif text.lower() == 'groupcreator':
                    group = gye.getGroup(to)
                    gye.sendMessage(to, "This person is the group creator.")
                    GS = group.creator.mid
                    gye.sendContact(to, GS)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'groupid':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[ ID Group : ]\n" + gid.id)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'grouppicture':
                    group = gye.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    gye.sendImageWithURL(to, path)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'groupname':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[ Nama Group : ]\n" + gid.name)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'qr':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = gye.reissueGroupTicket(to)
                            gye.sendMessage(to, "[ Group Qr ]\nhttps://gye.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            gye.sendMessage(to, "The qr group is not open, please open it first with the command {openqr}".format(str(settings["keyCommand"])))
#-------------------------------------------------------------------------------                            
                elif text.lower() == 'qr on':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            gye.sendMessage(to, "The qr group is open ! ")
                        else:
                            group.preventedJoinByTicket = False
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Successfully opened the qr group ! ")
#-------------------------------------------------------------------------------                            
                elif text.lower() == 'qr off':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            gye.sendMessage(to, "The qr group is closed ! ")
                        else:
                            group.preventedJoinByTicket = True
                            gye.updateGroup(group)
                            gye.sendMessage(to, "Successfully closed the qr group ! ")
#-------------------------------------------------------------------------------                            
                elif text.lower() == 'groupinfo':
                    group = gye.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Not found"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Closed"
                        gTicket = "There is no"
                    else:
                        gQr = "Open"
                        gTicket = "https://gye.me/R/ti/g/{}".format(str(gye.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ COLA_BOT ]"
                    ret_ += "\n╠➣ Group name : {}".format(str(group.name))
                    ret_ += "\n╠➣ MID Group : {}".format(group.id)
                    ret_ += "\n╠➣ Admin name : {}".format(str(gCreator))
                    ret_ += "\n╠➣ member : {}".format(str(len(group.members)))
                    ret_ += "\n╠➣ Invited members : {}".format(gPending)
                    ret_ += "\n╠➣ Group Qr : {}".format(gQr)
                    ret_ += "\n╠➣ Group Qr : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    gye.sendMessage(to, str(ret_))
                    gye.sendImageWithURL(to, path)
#-------------------------------------------------------------------------------                    
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        gye.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = gye.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = gye.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        gye.sendMessage(to, str(ret_))
#-------------------------------------------------------------------------------
                elif text.lower() == 'clearban':
                        settings["blacklist"] = {}
                        gye.sendMessage(msg.to,"➲ Done")
                        ais.sendMessage(msg.to,"➲ Done")
                        ki2.sendMessage(msg.to,"➲ Done")
                        ais.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
                        ki2.sendMessage(msg.to,"➲ Blacklist Dibersihkan")
#-------------------------------------------------------------------------------                        
                elif text.lower() == 'check bot':        
                        gye.sendMessage(msg.to,"Checking Bot")
                        ais.sendMessage(to,"=========================\n/BØT [ ² ] : เรามีหน้าที่ดูแลคุณ \n=========================")
                        ki2.sendMessage(to,"=========================\n/BØT [ ³ ] : เรามีหน้าที่ดูแลคุณ \n=========================")
                        gye.sendMessage(msg.to,"speedbot")
#-------------------------------------------------------------------------------                        
                elif text.lower() == 'check bot1':
                        gye.sendMessage(msg.to,"➲ BOT_Protect ¹")
                        ais.sendMessage(msg.to,"➲ BOT_Protect ²")
                        ki2.sendMessage(msg.to,"➲ BOT_Protect ³")
                        ki2.sendMessage(msg.to,"➲ The bot are still working!")
#-------------------------------------------------------------------------------                        
                elif text.lower() == 'check bot2':
                        gye.sendMessage(msg.to,"====BOT_COLA====")
                        ais.sendMessage(msg.to,"➲ By Cola 🇹🇭 ")
                        ki2.sendMessage(msg.to,"➲ By Cola 🇹🇭 ")
                        ais.sendMessage(msg.to,"➲ ² Report")
                        ki2.sendMessage(msg.to,"➲ ³ Report")
                        gye.sendMessage(msg.to,"====BOT_COLA====")
#-------------------------------------------------------------------------------                        
                elif msg.text in ["flat"]:
                  if msg._from in admin: 
                    settings["wblacklist"] = True
                    gye.sendMessage(msg.to,"Please send the contactor")    
#-------------------------------------------------------------------------------                        
                elif msg.text in ["unbancontact"]:
                        settings["dblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
#-------------------------------------------------------------------------------                        
                elif msg.text in ["flatwash"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"Delete all banned accounts.")        
#-------------------------------------------------------------------------------
                elif text.lower() == 'banlist':
                        if settings["blacklist"] == {}:
                            gye.sendMessage(msg.to,"Tidak Ada Banlist")
                        else:
                            gye.sendMessage(msg.to,"Daftar Banlist")
                            num=1
                            msgs="═══T E R S A N G K A═══"
                            for mi_d in settings["blacklist"]:
                                msgs+="\n[%i] %s" % (num, gye.getContact(mi_d).displayName)
                                num=(num+1)
                            msgs+="\n═══T E R S A N G K A═══\n\nTotal Tersangka :  %i" % len(settings["blacklist"])
                            gye.sendMessage(msg.to, msgs)
#-------------------------------------------------------------------------------
                elif msg.text.lower().startswith("kick"):
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"][0]["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(GUE).kickoutFromGroup(msg.to,[target])
                           except:
                               random.choice(GUE).sendText(msg.to,"Error")
#-------------------------------------------------------------------------------
                elif text.lower() == 'botkick':
                        if msg.toType == 2:
                            print ("[ 19 ] B O T _ K I C K")
                            _name = msg.text.replace("kickallmember","")
                            gs = ais.getGroup(msg.to)
                            gs = ki2.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                gye.sendMessage(msg.to,"Not Found")
                            else:
                                for target in targets:
                                    if not target in Bots:
                                        if not target in Owner:
                                            if not target in admin:
                                                try:
                                                    klist=[line,ais,ki2]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    gye.sendMessage(msg.to,"") 
#-------------------------------------------------------------------------------          
                elif text.lower() == 'tack':
                    group = gye.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        gye.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        gye.sendMessage(to, "All tags {} people".format(str(len(nama))))
#===============================================================================[gyeMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] COLA _ BOT _ PREVENT")
            try:
                if op.param3 in gyeMID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki2MID]
                elif op.param3 in gyeMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[gyeMID - ki3M
#===============================================================================[kiMID gyeMID]
                if op.param3 in aisMID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki2MID]
                elif op.param3 in aisMID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[kiMID ki3
#===============================================================================[ki2MID gyeMID]
                if op.param3 in ki2MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID kiMID]
                elif op.param3 in ki2MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki2MID ki3MID]
                
#===============================================================================[ki3MID gyeMID]
                if op.param3 in ki3MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID kiMID]
                elif op.param3 in ki3MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki2MID]
                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki3MID ki4MID]
                
#===============================================================================[ki4MID gyeMID]
                if op.param3 in ki4MID:
                    if op.param2 in gyeMID:
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                    else:
                        G = gye.getGroup(op.param1)
                        gye.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        gye.updateGroup(G)
                        invsend = 0
                        Ticket = gye.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = gye.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        gye.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        gye.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID kiMID]
                elif op.param3 in ki4MID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                    else:
                        G = ais.getGroup(op.param1)
                        ais.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ais.updateGroup(G)
                        invsend = 0
                        Ticket = ais.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ais.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ais.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ais.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki2MID]
                elif op.param3 in ki4MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        ki2.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        invsend = 0
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        gye.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ais.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                        G.preventedJoinByTicket(G)
                        ki2.updateGroup(G)
                        settings["blacklist"][op.param2] = True
#-------------------------------------------------------------------------------[ki4MID ki3MID]
                elif op.param2 not in Bots:
                    if op.param2 in admin:
                        pass
#-------------------------------------------------------------------------------                      
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")                       
                else:
                    pass
            except:
                pass
#-------------------------------------------------------------------------------
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in admin:
                    pass
                elif settings["inviteprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in admin:
                            pass
                        elif settings["cancelprotect"] == True:
                            settings["blacklist"][op.param2] = True
                            random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])	
#-------------------------------------------------------------------------------
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in admin and Bots and Owner:
                    pass
                elif settings["qrprotect"] == True:
                    settings["blacklist"][op.param2] = True
                    G = ais.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ais.updateGroup(G)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    gye.sendMessage(op.param1,"พบการเปิดลิ้งค์กลุ่ม")
            else:
                gye.sendMessage(op.param1,"")
#-------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if text.lower() == '/ti/g/':    
                if settings["join ticket"] == True:
                    link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                    links = link_re.findall(text)
                    n_links = []
                    for l in links:
                        if l not in n_links:
                            n_links.append(l)
                    for ticket_id in n_links:
                        group = gye.findGroupByTicket(ticket_id)
                        gye.acceptGroupInvitationByTicket(group.id,ticket_id)
                        gye.sendMessage(to, "Berhasil masuk ke group %s" % str(group.name))
#-------------------------------------------------------------------------------                        
    except Exception as error:
        logError(error)                        
#-------------------------------------------------------------------------------
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        gye.acceptGroupInvitation(op.param1)
        ais.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
    except Exception as e:
        gye.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
#-------------------------------------------------------------------------------
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        gye.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))
#-------------------------------------------------------------------------------
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
#-------------------------------------------------------------------------------
