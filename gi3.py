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

# Ini Untuk Login Via Lik Dan Via Emal
#gye = LINE()
#gye = LINE("Email","Password")
#gye.log("Auth Token : " + str(gye.authToken))
#channelToken = gye.getChannelResult()
#gye.log("Channel Token : " + str(channelToken))

# Silahkan Edit Sesukamu
# Asalkan Rapih Dan Respon
# jika ingin login Via qr Ganti Saja
# Atau Login Via Emal
# Mudeng Orang kalo Ra Mudeng
# Sungguh Terlalu
# Jangan Lupa Add Admin 
# id Line ( aisyagye )
#==============================================================================#
botStart = time.time()
#kalo mau login code qr disini pake
gye = LINE()
gye.log("Auth Token : " + str(gye.authToken))
channelToken = gye.getChannelResult()
gye.log("Channel Token : " + str(channelToken))

ais = LINE()
ais.log("Auth Token : " + str(ais.authToken))
channelToken = ais.getChannelResult()
ais.log("Channel Token : " + str(channelToken))

ki2 = LINE()
ki2.log("Auth Token : " + str(ki2.authToken))
channelToken = ki2.getChannelResult()
ki2.log("Channel Token : " + str(channelToken))


#kalo mau login menggunakan token
#gunakan disini hapus tanda pagarnya 
#yg atas dinpagar atau bisa juga token di atas 
#di dalam tanda LINE ("TOKEN MU ")
#gye = LINE("Et6qM8UeTce5bGsZG4te.ee6vQU/1ppqr93nt9QLUZG.b5fsCbuxW7zZRtrK5U/74k/53Abd5dWPxfdtLy9bL9I=")
#ais = LINE("Etska0dbjsHvPgZKwmj9.EikS5M3O+L4fOqxjjVgLsq.KlWfvmGVaXdM0yvKM8WGKARpcbAbiKVF9yORPt8QBJw=")
#ki2 = LINE("EtQsqzdJMWn73m72Gup0.OdjJmVnqXLeaZxpJzxDMOa.Z+6ApCht+0H1NeyX50QMD0Yq8oIhYyJ14Yg2yoM/tfc=")
#ki3 = LINE("EtDOOeYj4Rvl5PVfOEaa.ETpCu8czFapUIJQDqIA82G.tcOaI+VmHhWwMbyDL/7yXupWfdIvUJh80yWzu/UJXp8=")
#ki4 = LINE("EtWyu42OHWKSaxPHY3yd.jTri3xzV4E2Z1xvWxjTrRq.s1oy5gbYMT2haZV7l6yzV0bp5gONcnu+bGSSJ1mbT0c=")

KAC = [gye,ais,ki2]
GUE = [ais,ki2] # ini jangan luh hapus peak ini fungsi Ciak alias kick
#maksudnya agar bot sb/induk gak ikutan nge kick Mudeng ora
gyeMID = gye.profile.mid
aisMID = ais.profile.mid
ki2MID = ki2.profile.mid
Bots = ["u78d3b315b4268d7b3654f8486e07e5e0","u7b4abcec38a39e8ab52b0c939eb79fa9","u3bc28db881a917b7e8add49a47e6df72"]
creator = ["u78d3b315b4268d7b3654f8486e07e5e0","u7b4abcec38a39e8ab52b0c939eb79fa9","u3bc28db881a917b7e8add49a47e6df72"]
Owner = ["u78d3b315b4268d7b3654f8486e07e5e0","u7b4abcec38a39e8ab52b0c939eb79fa9","u3bc28db881a917b7e8add49a47e6df72"]
admin = ["u78d3b315b4268d7b3654f8486e07e5e0","u7b4abcec38a39e8ab52b0c939eb79fa9","u3bc28db881a917b7e8add49a47e6df72"]

gyeProfile = gye.getProfile()
aisProfile = ais.getProfile()
ki2Profile = ki2.getProfile()

lineSettings = gye.getSettings()
aisSettings = ais.getSettings()
ki2Settings = ki2.getSettings()

oepoll = OEPoll(gye)
oepoll1 = OEPoll(ais)
oepoll2 = OEPoll(ki2)

responsename = gye.getProfile().displayName
responsename2 = ais.getProfile().displayName
responsename3 = ki2.getProfile().displayName
#==============================================================================#




with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
    
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = gyeProfile.displayName
myProfile["statusMessage"] = gyeProfile.statusMessage
myProfile["pictureStatus"] = gyeProfile.pictureStatus

readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

#==============================================================================#

read = json.load(readOpen)
settings = json.load(settingsOpen)

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    gye.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        gye.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        
def helpmessage():
    helpMessage = "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣       H-A-C-K_B-O-T" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣            หน้า 1" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ คำสั่ง1" + "\n" + \
                  "║͜͡☆➣ คำสั่ง2" + "\n" + \
                  "║͜͡☆➣ แทค" + "\n" + \
                  "║͜͡☆➣ เรา" + "\n" + \
                  "║͜͡☆➣ Sp" + "\n" + \
                  "║͜͡☆➣ เช็ค" + "\n" + \
                  "║͜͡☆➣ แจ๊ะ@" + "\n" + \
                  "║͜͡☆➣ แจ๊ะๆ" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      H-A-C-K_B-O-T" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech = "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      H-A-C-K_B-O-T" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣            หน้า 2" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ คำสั่ง1" + "\n" + \
                  "║͜͡☆➣ คำสั่ง2" + "\n" + \
                  "║͜͡☆➣ ป้องกัน 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ ป้องกันลิ้งค์「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ ป้องกันเชิญ 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ ป้องกันยกเชิญ「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ AutoAdd 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ AutoJoin 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ ออกออโต้ 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ CheckSticker 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ AutoRead 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ DetectMention 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ Join link 「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ แอดกลุ่ม" + "\n" + \
                  "║͜͡☆➣ ไอดีกลุ่ม" + "\n" + \
                  "║͜͡☆➣ ชื่อกลุ่ม" + "\n" + \
                  "║͜͡☆➣ ดูรูปกลุ่ม" + "\n" + \
                  "║͜͡☆➣ GroupList" + "\n" + \
                  "║͜͡☆➣ GroupMemberList" + "\n" + \
                  "║͜͡☆➣ GroupInfo" + "\n" + \
                  "║͜͡☆➣ ลิ้ง" + "\n" + \
                  "║͜͡☆➣ ลิ้ง เปิด/ปิด" + "\n" + \
                  "║͜͡☆➣ Mimic on" + "\n" + \
                  "║͜͡☆➣ Mimic off" + "\n" + \
                  "║͜͡☆➣ MimicAdd" + "\n" + \
                  "║͜͡☆➣ MimicDel" + "\n" + \
                  "║͜͡☆➣ จับอ่าน「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ จับอ่าน" + "\n" + \
                  "║͜͡☆➣ รีจับอ่าน" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      H-A-C-K_B-O-T" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate = "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      H-A-C-K_B-O-T" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣            หน้า 3" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣ AdminLit" + "\n" + \
                  "║͜͡☆➣ OwnerList" + "\n" + \
                  "║͜͡☆➣ BanContact" + "\n" + \
                  "║͜͡☆➣ UnbanContact" + "\n" + \
                  "║͜͡☆➣ BanList" + "\n" + \
                  "║͜͡☆➣ Clearban" + "\n" + \
                  "║͜͡☆➣ รีบอท" + "\n" + \
                  "║͜͡☆➣ ออน" + "\n" + \
                  "║͜͡☆➣ About" + "\n" + \
                  "║͜͡☆➣ Me" + "\n" + \
                  "║͜͡☆➣ MyMid" + "\n" + \
                  "║͜͡☆➣ Midnya @" + "\n" + \
                  "║͜͡☆➣ MyName" + "\n" + \
                  "║͜͡☆➣ MyBio" + "\n" + \
                  "║͜͡☆➣ MyPicture" + "\n" + \
                  "║͜͡☆➣ MyVideoProfile" + "\n" + \
                  "║͜͡☆➣ MyCover" + "\n" + \
                  "║͜͡☆➣ StealContact @" + "\n" + \
                  "║͜͡☆➣ StealMid @" + "\n" + \
                  "║͜͡☆➣ StealName「Mention」" + "\n" + \
                  "║͜͡☆➣ StealBio @" + "\n" + \
                  "║͜͡☆➣ StealPicture @" + "\n" + \
                  "║͜͡☆➣ StealVideoProfile @" + "\n" + \
                  "║͜͡☆➣ StealCover @" + "\n" + \
                  "║͜͡☆➣ CloneProfile @" + "\n" + \
                  "║͜͡☆➣ RestoreProfile" + "\n" + \
                  "║͜͡☆➣ แอดกลุ่ม" + "\n" + \
                  "║͜͡☆➣ ไอดีกลุ่ม" + "\n" + \
                  "║͜͡☆➣ ชื่อกลุ่ม" + "\n" + \
                  "║͜͡☆➣ ดูรูปกลุ่ม" + "\n" + \
                  "║͜͡☆➣ ลิ้ง" + "\n" + \
                  "║͜͡☆➣ ลิ้ง「เปิด/ปิด」" + "\n" + \
                  "║͜͡☆➣ GroupList" + "\n" + \
                  "║͜͡☆➣ GroupMemberList" + "\n" + \
                  "║͜͡☆➣ GroupInfo" + "\n" + \
                  "║͜͡☆➣ แจ๊ะ@" + "\n" + \
                  "║͜͡☆➣ แจ๊ะๆ"+ "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      H-A-C-K_B-O-T" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpTranslate
#==============================================================================#
def helpprotect():
    helpProtect = "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      ชุดคำ สั่ง ป้องกัน" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║/ ป้องกัน「เปิด/ปิด」กันลบ" + "\n" + \
                  "║/ ป้องกันลิ้ง「เปิด/ปิด」กันลิ้ง" + "\n" + \
                  "║/ ป้องกันเชิญ「เปิด/ปิด」กันเชิญ" + "\n" + \
                  "║/ ป้องกันยกเชิญ「เปิด/ปิด」กันยก" + "\n" + \
                  "║/ เปิดหมด「เปิด/ปิด」กันทั้งหมด" + "\n" + \
                  "║/ มา = เรียกคิกเข้ากลุ่ม" + "\n" + \
                  "║/ ไป = เรียกคิกออกกลุ่ม" + "\n" + \
                  "║/ บอท = เช็คคทบอท" + "\n" + \
                  "║/ บาย = บอททั้งหมดออกกลุ่ม" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      ชุดคำ สั่ง เช็คบอท" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║/ Sp = ความเร็วบอท" + "\n" + \
                  "║/ สปีด = เช็คความเร็วบอททั้งหมด" + "\n" + \
                  "║/ รายงานตัว1 = เช็คชื่อบอท" + "\n" + \
                  "║/ รายงานตัว2 = เช็คชื่อบอท" + "\n" + \
                  "║/ ออน = เช็คเวลาทำงานบอท" + "\n" + \
                  "║/ เช็ค = เช็คคำสั่งที่「เปิด/ปิด」" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      ชุดคำ สั่ง ส่วนตัว" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║/ เรา = คทตัวเรา" + "\n" + \
                  "║/ Mเรา = MID เรา" + "\n" + \
                  "║/ ชื่อเรา = ชื่อไลน์เรา" + "\n" + \
                  "║/ ตัสเรา = สเตตัสเรา" + "\n" + \
                  "║/ รูปเรา = รูปไลน์เรา" + "\n" + \
                  "║/ ปกเรา = รูปปกไลน์เรา" + "\n"+ \
                  "║/ ขโมยชื่อ = ดึงชื่อ @" + "\n"+ \
                  "║/ ขโมยรูป = ดึงรูป @" + "\n"+ \
                  "║/ ขโมยปก = ดึงปก @" + "\n"+ \
                  "║/ ขโมยM = ดึงM @" + "\n"+ \
                  "║/ ขโมยตัส = ดึงตัส @" + "\n"+ \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║͜͡☆➣      ชุดคำ สั่ง แบน/ลบ" + "\n" + \
                  "╰════════╬♥╬════════╯" + "\n" + \
                  "╭════════╬♥╬════════╮" + "\n" + \
                  "║/ แจ๊ะ = ลบเฉพาะคนที่แทค@" + "\n" + \
                  "║/ แจ๊ะๆ = ลบทุกคน" + "\n" + \
                  "╰════════╬♥╬════════╯"
    return helpProtect
#==============================================================================#
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
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(settings["keyCommand"]):
        cmd = pesan.replace(settings["keyCommand"],"")
    else:
        cmd = "Undefined command"
    return cmd        


def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] C O L A - H A C K - B O T")
            return
#-------------------------------------------------------------------------------
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        gye.sendMessage(msg.to,"Itu tidak berkomentar")
                elif settings["dblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblack"] = False
                    else:
                        settings["dblack"] = False
                        gye.sendMessage(msg.to,"Tidak ada dalam daftar hitam")
#-------------------------------------------------------------------------------
                elif settings["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        gye.sendMessage(msg.to,"sudah masuk daftar hitam")
                        settings["wblacklist"] = False
                    else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                elif settings["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        gye.sendMessage(msg.to,"Done")
                        settings["dblacklist"] = False
                    else:
                        settings["dblacklist"] = False
                        gye.sendMessage(msg.to,"Done")
                        
                       
#-------------------------------------------------------------------------------
        if op.type == 25:
            print ("[ 25 ] GYEVHA BOTS TIGA")
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
#==============================================================================#
                if text.lower() == 'คำสั่ง':
                    helpMessage = helpmessage()
                    gye.sendMessage(to, str(helpMessage))
                    gye.sendContact(to, "u104e95aaefb53cf411f77353f6a96ece")
                    gye.sendMessage(to, "=============================\nBotName: COLA HACK BOT\nVersion: COLA BOT3\nThanks to: @Cola  @HACK_BOT\n=============================")
                elif text.lower() == 'คำสั่ง1':
                    helpTextToSpeech = helptexttospeech()
                    gye.sendMessage(to, str(helpTextToSpeech))
                    gye.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
                elif text.lower() == 'คำสั่ง2':
                    helpTranslate = helptranslate()
                    gye.sendMessage(to, str(helpTranslate))
                    gye.sendMessage(to, "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
                elif text.lower() == '/ป้องกัน':
                    helpProtect = helpprotect()
                    gye.sendMessage(to, str(helpProtect))
                    gye.sendMessage(to, "=============================\nBotName: COLA HACK BOT\nVersion: COLA BOT3\nThanks to: @Cola  @HACK_BOT\n=============================")
#==============================================================================#
                elif text.lower() == 'sp':
                    start = time.time()
                    gye.sendMessage(to, "ความเร็วบอท...")
                    elapsed_time = time.time() - start
                    gye.sendMessage(to,format(str(elapsed_time)))
#==============================================================================#
                elif text.lower() == 'สปีด':
                    start = time.time()
                    gye.sendMessage(to, "กำลังเช็คความเร็ว")
                    elapsed_time = time.time() - start
                    gye.sendMessage(to, "%sseconds" % (elapsed_time))    
                    ais.sendMessage(to, "%sseconds" % (elapsed_time))    
                    ki2.sendMessage(to, "%sseconds" % (elapsed_time))    
                    #ki3.sendMessage(to, "%sseconds" % (elapsed_time))    
                    #ki4.sendMessage(to, "%sseconds" % (elapsed_time))    
                    #ki5.sendMessage(to, "%sseconds" % (elapsed_time))
                    gye.sendMessage(to, "เช็คความเร็วเสร็จ")
#==============================================================================#                  
                elif text.lower() == 'รีบอท':    
                    gye.sendMessage(to, "กำลังรีบอท รอสักครู่...")
                    time.sleep(5)
                    gye.sendMessage(to, "รีบอทแล้วล็อคอินใหม่ด้วย")
                    restartBot()
                elif text.lower() == 'ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    gye.sendMessage(to, "ระยะเวลาออน {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ABISHEK SINGH"
                        creator = gye.getContact(owner)
                        contact = gye.getContact("ua287bd3b899219d0da256ea2a2217521")
                        grouplist = gye.getGroupIdsJoined()
                        contactlist = gye.getAllContactIds()
                        blockedlist = gye.getBlockedContactIds()
                        ret_ = "╭════════╬♥╬════════╮\nStatus Bots\n ╰════════╬♥╬════════╯\n ╭════════╬♥╬════════╮\n"
                        ret_ += "\n╠ akun : {}".format(contact.displayName)
                        ret_ += "\n╠ group : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ teman : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ Blokir : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ About Selfbot ]"
                        ret_ += "\n╠ Version : Premium"
                        ret_ += "\n╠ Creator : {}".format(creator.displayName)
                        ret_ += "\n╰════════╬♥╬════════╯\n\nGYEVHA BOTS╭════════╬♥╬════════╮\n╰════════╬♥╬════════╯"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'เช็ค':
                    try:
                        ret_ = "╭════════╬♥╬════════╮\n║͜͡☆➣ ♥ Status Bots ♥\n╰═════════╬♥╬════════╯\n╭═════════╬♥╬════════╮\n"
                        if settings["protect"] == True: ret_ += "║͜͡☆➣ ป้องกัน ✔️"
                        else: ret_ += "║͜͡☆➣  ป้องกัน ❌"
                        if settings["qrprotect"] == True: ret_ += "\n║͜͡☆➣ ป้องกันลิ้ง ✔️"
                        else: ret_ += "\n║͜͡☆➣ ป้องกันลิ้ง ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n║͜͡☆➣ ป้องกันเชิญ ✔️"
                        else: ret_ += "\n║͜͡☆➣ ป้องกันเชิญ ❌"
                        if settings["cancelprotect"] == True: ret_ += "\n║͜͡☆➣ ป้องกันยกเชิญ ✔️"
                        else: ret_ += "\n║͜͡☆➣ ป้องกันยกเชิญ ❌"
                        if settings["autoAdd"] == True: ret_ += "\n║͜͡☆➣ Auto Add ✔️"
                        else: ret_ += "\n║͜͡☆➣ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n║͜͡☆➣ Auto Join ✔️"
                        else: ret_ += "\n║͜͡☆➣ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n║͜͡☆➣ Auto Leave ✔️"
                        else: ret_ += "\n║͜͡☆➣ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n║͜͡☆➣ Auto Read ✔️"
                        else: ret_ += "\n║͜͡☆➣ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n║͜͡☆➣ Check Sticker ✔️"
                        else: ret_ += "\n║͜͡☆➣ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n║͜͡☆➣ Detect Mention ✔️"
                        else: ret_ += "\n║͜͡☆➣ Detect Mention ❌"
                        ret_ += "\n╰════════╬♥╬════════╯\n╭════════╬♥╬════════╮\n║͜͡☆➣ ♥ GYEVHA BOTS ♥\n╰════════╬♥╬════════╯"
                        gye.sendMessage(to, str(ret_))
                    except Exception as e:
                        gye.sendMessage(msg.to, str(e))
                        
                elif msg.text.lower().startswith("spaminvite "):
                   #if msg._from in admin:
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
                            #else:
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
              #      else:
               #         gye.sendMessage(msg.to,"Owner Permission Required")
#-------------------------------------------------------------------------------
                elif text.lower() == 'adminlist':
                #    if msg._from in Owner:
                        if admin == []:
                            gye.sendMessage(msg.to,"The Adminlist is empty")
                        else:
                            gye.sendMessage(msg.to,"WAITING..")
                            mc = "╔═══════════════\n╠WAR BOT\n╠══✪〘 Admin List 〙✪═══\n"
                            for mi_d in admin:
                                mc += "╠✪ " +gye.getContact(mi_d).displayName + "\n"
                            gye.sendMessage(msg.to,mc + "╠═══════════════\n╠✪〘 ABISHEK 〙\n╚═══════════════")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ป้องกัน เปิด':
                        if settings["protect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิด!")
                        else:
                            settings["protect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิด!")
                                
                elif text.lower() == 'ป้องกัน ปิด':
                        if settings["protect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันปิด!")
                        else:
                            settings["protect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันปิด!")
#----------------------------------------------------------------------------------------                        
                elif text.lower() == 'ป้องกันลิ้ง เปิด':
                        if settings["qrprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิดลิ้งเปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิดลิ้งเปิด!")
                        else:
                            settings["qrprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิดลิ้งเปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิดลิ้งเปิด!")
                                
                elif text.lower() == 'ป้องกันลิ้ง ปิด':
                        if settings["qrprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิดลิ้งปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิดลิ้งปิด!")
                        else:
                            settings["qrprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิดลิ้งปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันเปิดลิ้งปิด!")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ป้องกันเชิญ เปิด':
                        if settings["inviteprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเชิญเปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันเชิญเปิด!")
                        else:
                            settings["inviteprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเชิญเปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันเชิญเปิด!")
                                
                elif text.lower() == 'ป้องกันเชิญ ปิด':
                        if settings["inviteprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเชิญปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันเชิญปิด!")
                        else:
                            settings["inviteprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันเชิญปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันเชิญปิด!")
#-------------------------------------------------------------------------------
                elif text.lower() == 'ป้องกันยกเชิญ เปิด':
                        if settings["cancelprotect"] == True:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันยกเชิญเปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันยกเชิญเปิด!")
                        else:
                            settings["cancelprotect"] = True
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันยกเชิญเปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันยกเชิญเปิด!")
                                
                elif text.lower() == 'ป้องกันยกเชิญ ปิด':
                        if settings["cancelprotect"] == False:
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันยกเชิญปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันยกเชิญปิด!")
                        else:
                            settings["cancelprotect"] = False
                            if settings["lang"] == "JP":
                                gye.sendMessage(msg.to,"➲ ป้องกันยกเชิญปิด!")
                            else:
                                gye.sendMessage(msg.to,"➲ ป้องกันยกเชิญปิด!")
#-------------------------------------------------------------------------------
                elif text.lower() == 'เปิดหมด เปิด':
                        settings["protect"] = True
                        settings["qrprotect"] = True
                        settings["inviteprotect"] = True
                        settings["cancelprotect"] = True
                        gye.sendMessage(msg.to,"ป้องกัน เปิด")
                        gye.sendMessage(msg.to,"ป้องกันลิ้ง เปิด")
                        gye.sendMessage(msg.to,"ป้องกันเชิญ เปิด")
                        gye.sendMessage(msg.to,"ป้องกันยกเชิญ เปิด")
                        gye.sendMessage(msg.to,"➲ ชุดป้องกันทั้งหมด เปิด!")
                        		            
                elif text.lower() == 'เปิดหมด ปิด':
                        settings["protect"] = False
                        settings["qrprotect"] = False
                        settings["inviteprotect"] = False
                        settings["cancelprotect"] = False
                        gye.sendMessage(msg.to,"ป้องกัน ปิด")
                        gye.sendMessage(msg.to,"ป้องกันลิ้ง ปิด")
                        gye.sendMessage(msg.to,"ป้องกันเชิญ ปิด")
                        gye.sendMessage(msg.to,"ป้องกันยกเชิญ ปิด")
                        gye.sendMessage(msg.to,"➲ ชุดป้องกันทั้งหมด ปิด!")
#-------------------------------------------------------------------------------
                elif text.lower() == 'แอดออโต้ เปิด':
                    settings["autoAdd"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Add")
                elif text.lower() == 'แอดออโต้ ปิด':
                    settings["autoAdd"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Add")
                elif text.lower() == 'เข้าออโต้ เปิด':
             #     if msg._from in Owner:    
                    settings["autoJoin"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Join")
                elif text.lower() == 'เข้าออโต้ ปิด':
                #  if msg._from in Owner:    
                    settings["autoJoin"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Join")
                elif text.lower() == 'ออกออโต้ เปิด':
               #   if msg._from in Owner:
                    settings["autoLeave"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Leave")
                elif text.lower() == 'ออกออโต้ ปิด':
             #     if msg._from in Owner:
                    settings["autoLeave"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Leave")
                elif text.lower() == 'อ่านออโต้  เปิด':
                    settings["autoRead"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Read")
                elif text.lower() == 'อ่านออโต้ ปิด':
                    settings["autoRead"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Read")
                elif text.lower() == 'เช็คติ๊ก เปิด':
                    settings["checkSticker"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Check Details Sticker")
                elif text.lower() == 'เช็คติ๊ก ปิด':
                    settings["checkSticker"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                    settings["datectMention"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                    settings["datectMention"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Detect Mention")
                elif text.lower() == 'เข้าลิ้งค์ เปิด':
                    settings["autoJoinTicket"] = True
                    gye.sendMessage(to, "Berhasil mengaktifkan Auto Join Link")
                elif text.lower() == 'เข้าลิ้งค์  ปิด':
                    settings["autoJoinTicket"] = False
                    gye.sendMessage(to, "Berhasil menonaktifkan Auto Join Link")                    
#========================เรียกบอท เข้า/ออก======================================#
                elif msg.text.lower() == 'บอท':
                        gye.sendContact(to, gyeMID)
                        ais.sendContact(to, aisMID)
                        ki2.sendContact(to, ki2MID)
                elif text.lower() in ["ออกไป","ไป","นนท์ไป"]:    
                    #gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                elif text.lower() in ["บาย"]:    
                    gye.leaveGroup(msg.to)
                    ais.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                elif text.lower() in ["เข้ามา","มา","คิกมา","นนท์มา"]:    
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
                    ais.sendMessage(msg.to,"🌟 ⭐️ เรามีหน้าที่ป้องกันคุณ ¹ ⭐️ 🌟")
                    ki2.sendMessage(msg.to,"🌟 ⭐️ เรามีหน้าที่ป้องกันคุณ ² ⭐️ 🌟")
                
                elif text.lower() == 'เรา':
                    sendMessageWithMention(to, gyeMID)
                    gye.sendContact(to, gyeMID)
                elif text.lower() == 'Mเรา':
                    gye.sendMessage(msg.to,"[MID ของเรา]\n" +  gyeMID)
                elif text.lower() == 'ชื่อเรา':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[ชื่อ ไลน์ เรา]\n" + me.displayName)
                elif text.lower() == 'ตัสเรา':
                    me = gye.getContact(gyeMID)
                    gye.sendMessage(msg.to,"[ตัส]\n" + me.statusMessage)
                elif text.lower() == 'รูปเรา':
                    me = gye.getContact(gyeMID)
                    gye.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'วิดีโอเรา':
                    me = gye.getContact(gyeMID)
                    gye.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'รูปปกเรา':
                    me = gye.getContact(gyeMID)
                    cover = gye.getProfileCoverURL(gyeMID)    
                    gye.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("ขโมยคท "):
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
                elif msg.text.lower().startswith("ขโมยM "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ ขโมย Mid ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        gye.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("ขโมยชื่อ "):
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
                            gye.sendMessage(msg.to, "[ ขโมย ชื่อ ]\n" + contact.displayName)
                elif msg.text.lower().startswith("ขโมยตัส "):
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
                            gye.sendMessage(msg.to, "[ ขโมย ตัส ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("ขโมยรูป "):
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
                elif msg.text.lower().startswith("ขโมยวิดีโอ "):
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
                elif msg.text.lower().startswith("ขโมยปก "):
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
                elif msg.text.lower().startswith("ก็อป "):    
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            gye.cloneContactProfile(contact)
                            gye.sendMessage(msg.to, "ก็อปสำเร็จรอโปรเส็จ")
                        except:
                            gye.sendMessage(msg.to, "ก็อปล้มเหลว")
                elif text.lower() == 'กลับคืน':    
                    try:
                        gyeProfile.displayName = str(myProfile["displayName"])
                        gyeProfile.statusMessage = str(myProfile["statusMessage"])
                        gyeProfile.pictureStatus = str(myProfile["pictureStatus"])
                        gye.updateProfileAttribute(8, gyeProfile.pictureStatus)
                        gye.updateProfile(gyeProfile)
                        gye.sendMessage(msg.to, "กลับคืนสำเร็จรอโปรเส็จ")
                    except:
                        gye.sendMessage(msg.to, "กลับคืนล้มเหลว")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            gye.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            gye.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            gye.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        gye.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+gye.getContact(mi_d).displayName
                        gye.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
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
#==============================================================================#
                elif text.lower() == 'แอดกลุ่ม':
                    group = gye.getGroup(to)
                    gye.sendMessage(to, "คนนี้คือผู้สร้างกลุ่ม")
                    GS = group.creator.mid
                    gye.sendContact(to, GS)
                elif text.lower() == 'ไอดีกลุ่ม':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[ไอดี ของกลุ่ม : ]\n" + gid.id)
                elif text.lower() == 'ดูรูปกลุ่ม':
                    group = gye.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    gye.sendImageWithURL(to, path)
                elif text.lower() == 'ชื่อกลุ่ม':
                    gid = gye.getGroup(to)
                    gye.sendMessage(to, "[ชื่อ ของกลุ่ม : ]\n" + gid.name)
                elif text.lower() == 'ลิ้ง':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = gye.reissueGroupTicket(to)
                            gye.sendMessage(to, "[ ลิ้งค์ของกลุ่ม ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            gye.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'ลิ้ง เปิด':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            gye.sendMessage(to, "เปิดแล้ว!")
                        else:
                            group.preventedJoinByTicket = False
                            gye.updateGroup(group)
                            gye.sendMessage(to, "เปิดแล้ว!")
                elif text.lower() == 'ลิ้ง ปิด':
                    if msg.toType == 2:
                        group = gye.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            gye.sendMessage(to, "ปิดแล้ว!")
                        else:
                            group.preventedJoinByTicket = True
                            gye.updateGroup(group)
                            gye.sendMessage(to, "ปิดแล้ว!")
                elif text.lower() == 'ข้อมูลกลุ่ม':
                    group = gye.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(gye.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ HACK-BOT ]"
                    ret_ += "\n╠ ชื่อ กลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ MID กลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ชื่อ แอดมิน : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ  : {}".format(gPending)
                    ret_ += "\n╠ ลิ้ง กลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งของ กลุ่ม : {}".format(gTicket)
                    ret_ += "\n╚══[ เสร็จ ]"
                    gye.sendMessage(to, str(ret_))
                    gye.sendImageWithURL(to, path)
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
                        
                elif text.lower() == 'รายงานตัว1':
                        gye.sendMessage(msg.to,"➲ HACK_BOT ¹")
                        ais.sendMessage(msg.to,"➲ HACK_BOT ²")
                        ki2.sendMessage(msg.to,"➲ HACK_BOT ³")
                        ki2.sendMessage(msg.to,"➲ บอทยังอยู่!")
                        
                elif text.lower() == 'รายงานตัว2':
                        gye.sendMessage(msg.to,"====HACK_BOT====")
                        ais.sendMessage(msg.to,"➲ 🇹🇭 ")
                        ki2.sendMessage(msg.to,"➲ 🇹🇭 ")
                        ais.sendMessage(msg.to,"➲ ² รายตัว")
                        ki2.sendMessage(msg.to,"➲ ³ รายตัว")
                        gye.sendMessage(msg.to,"====HACK_BOT====")
                        
                elif text.lower() == 'bancontact':
                        settings["wblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
                        
                elif msg.text in ["unbancontact"]:
                        settings["dblacklist"] = True
                        gye.sendMessage(msg.to,"Send Contact")
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
#=======================================================================================
                elif msg.text.lower().startswith("แจ๊ะ"):
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
                elif text.lower() == 'แจ๊ะ':
                        if msg.toType == 2:
                            print ("[ 19 ] KICK ALL MEMBER")
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
#==============================================================================#          
                elif text.lower() == 'แทค':
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
                        gye.sendMessage(to, "แทคทั้งหมด {} คน".format(str(len(nama))))          
                elif text.lower() == 'จับอ่าน เปิด':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                gye.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            gye.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            gye.sendMessage(msg.to,"➲ Jangan Songong Pake Sc Orang")
                            
                elif text.lower() == 'จับอ่าน ปิด':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        gye.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        gye.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'รีจับอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        gye.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        gye.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'จับอ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            gye.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = gye.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            gye.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        gye.sendMessage(receiver,"Lurking has not been set.")
                        
#===============================================================================[gyeMID - kiMID]
        if op.type == 19:
            print ("[ 19 ] GYEVHA BOTS KICK")
            try:
                if op.param3 in gyeMID:
                    if op.param2 in aisMID:
                        G = ais.getGroup(op.param1)
#                        ginfo = ki.getGroup(op.param1)
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
#                        ginfo = ais.getGroup(op.param1)
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
#                        ginfo = ki2.getGroup(op.param1)
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
#                        ginfo = gye.getGroup(op.param1)
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
#                        ginfo = gye.getGroup(op.param1)
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
#                        ginfo = ais.getGroup(op.param1)
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
#                        ginfo = ki.getGroup(op.param1)
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
#                        ginfo = gye.getGroup(op.param1)
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
#                        ginfo = gye.getGroup(op.param1)
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
#                        ginfo = ais.getGroup(op.param1)
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
#                        ginfo = ais.getGroup(op.param1)
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
#                        ginfo = ki2.getGroup(op.param1)
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
#                        ginfo = ki2.getGroup(op.param1)
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
#                        ginfo = gye.getGroup(op.param1)
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
#                        ginfo = gye.getGroup(op.param1)
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
#                        ginfo = ki.getGroup(op.param1)
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
#                        ginfo = ais.getGroup(op.param1)
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
#                        ginfo = ki2.getGroup(op.param1)
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
#                        ginfo = ki2.getGroup(op.param1)
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
                    elif settings["protect"] == True:
                        settings["blacklist"][op.param2] = True
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        random.choice(KAC).sendText(op.param1,"Don't Play bro...!")
                        
                else:
                    pass
            except:
                pass
#==============================================================================#
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
#==============================================================================#
       # if op.type == 55:
        #    print ("[ 55 ] GYEVHA BOTS EMPAT")
         #   if op.param1 in read["readPoint"]:
          #      _name = gye.getContact(op.param2).displayName
           #     tz = pytz.timezone("Asia/Jakarta")
           #     timeNow = datetime.now(tz=tz)
            #    timeHours = datetime.strftime(timeNow," (%H:%M)")
             #   read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
     #   backupData()
    #except Exception as error:
     #   logError(error)
#==============================================================================#
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
                        
    except Exception as error:
        logError(error)
#==============================================================================#
# Auto join if BOT invited to group
def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        gye.acceptGroupInvitation(op.param1)
        ais.acceptGroupInvitation(op.param1)
        ki2.acceptGroupInvitation(op.param1)
    except Exception as e:
        gye.log("[NOTIFIED_INVITE_INTO_GROUP] ERROR : " + str(e))
# Auto kick if BOT out to group
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,op.param2)
        else:
            pass
    except Exception as e:
        gye.log("[NOTIFIED_KICKOUT_FROM_GROUP] ERROR : " + str(e))

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)       
