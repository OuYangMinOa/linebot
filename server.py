from flask import Flask, request, abort         # flask 伺服器
import threading                                            #多現成
import random                                               # 隨機
from PIL import Image, ImageDraw, ImageFont # 圖片
import datetime                                             # 現在時間
from spuare_row import *                             # 平方數鏈
from download_google_image import *          # 爬蟲
import cv2                                                  # openv
import numpy as np                                      # 矩陣函數庫
from my_math import *                                   # 積分微分
from imgurpython import ImgurClient              # 上傳圖片
import time                                                     # 時間函示庫
from grabscreen import grab_screen              # 截圖
from client import*                                         # 上傳圖片
from functools import partial
from bfs import*                                            #到水問題
from QRCODE import *                                    # qrcode
import os                                       
global pin
global url_max,search_id,lib_you
pin = None
lib_you = {}
################ LinebotAPi#################
from linebot import (
    LineBotApi, WebhookHandler
)   
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,StickerSendMessage,ImageSendMessage
)
#############################################
app = Flask(__name__)

line_bot_api = LineBotApi('wJMb06yrUCxmFh10ZQOiibHTECj\
WHwZF1UuKjKF7NUVMBuglRrs95+U\
9/GQThd/EbKrm5ce/xFCayhgwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('10e397d4967b53597a0a83')


######### imgur ########################
client_id = 'b9ae77114a61'
client_secret = '720fc83b0d74815bf3a6e66'
##################################
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
def get_source(event):
    if event.source.type == 'user':  # 使用者
        return event.source.user_id, event.source.user_id
    elif event.source.type == 'group': # 聊天室
        return event.source.group_id, event.source.user_id
    elif event.source.type == 'room': # 群組
        return event.source.room_id, event.source.user_id
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global search_id,lib_you
    messages = '' 
    source_id, user_id= get_source(event) # 先取的來源
    ################ 測適用ID #####################
    maker = 'U3e4eca507a83989c933d200b5ec0228a'
    girl = 'U5e951347ff84bc8ab92c8e2a84256eb1'
    OuO_chat = 'Cf05cfae8d6d684de6b3d3a4150aa4aff'
    ################ 權限分類 #####################
    Permission = 0 
    add_t = "add.txt"
    eat_name = '餐廳.txt'
    if (source_id!=OuO_chat and source_id!= maker and source_id!= maker):
        file_name = 'list_id_2.txt'
        add_idlist(source_id,file_name) # 紀錄ID
        add_idlist(user_id,file_name)
        Permission = 1
        add_t = "add_2.txt"
    #######################################
    reply_dict ={} # 之後會儲存回復
    reply_mesg = ''  
    sticker_message = StickerSendMessage(
    package_id='1',
    sticker_id='1'
    )
    
    msg = (event.message.text).strip() # 使用者說的話
    
    # 接近所有指令的集合
    all_reply='''####以下為內建指令####
幹話, 獲得一個幹話
add 你要的指令,你要的回應
上車
開車
輔大物理
新聞 # 壞
積分,方程式,上界,下界 (目前只能對x積分)
微分,方程式 (目前只能對x微分)
降雨
天氣
溫度 # 壞
程序
地震
平方數鏈 串列大小
查詢影片 關鍵字
色情 關鍵字
google 關鍵字
翻譯 關鍵字
手語 字串
人數
歸一化 方程式 (自己算啦!
體積分 方程式 (r x y -> r θ ϕ 
數據大小
吃飯 (雖機抽午餐
新增吃飯 餐廳名稱(增加餐聽
太空
trivago
倒水問題,水瓶1,水瓶2,要的水量
這是+關鍵字,圖片的url(可有可無)
神的語言 123456(通常為六碼)
前四個字串為http
矩陣相乘 [[1,2],[3,4]]*[[q,b][c,a]]
qrcode url
後四個字串為.jpg
指令數量
指令
'''
    ################ 顯示在cmd上的資訊 ###################
    print('\n\r','-'*120)
    print(" 來自:",source_id,"，發言者: ",user_id)
    print('-'*120)
    print('\n 對話: '+ msg,end='\n 回應:')
    ######################################
    try:
        if (source_id in  lib_you): # 有使用 查詢影片 跟 google 功能的
            try :
                get_num = int(msg) -1 # 矩陣是從0開始
                get_url = lib_you[source_id][get_num]
                line_bot_api.push_message(source_id,TextSendMessage(text=str(get_url)))
                get_screen_url(str(get_url))
                time.sleep(1)
                url = get_img('D:/python/linebot/linebot/url_screen.png')
                line_bot_api.push_message(source_id,ImageSendMessage(
                    original_content_url=url,
                    preview_image_url=url
                ))
                return
            except Exception as e :
                pass
    except Exception as e :
        print(e)
        
    # 打開 add.txt
    if (not os.path.isfile(add_t)):
        # 如果不存在 開一個新
        with open(add_t,'w') as f:
            pass
    # 如果存在 讀取每一行 存起來
    with open(add_t,'r') as f:
        while 1:
            grt = f.readline().strip().split(',')
            if (grt == None or grt == '' or grt== []): 
                break
            try:
                reply_dict.update({grt[0]:grt[1]})
            except:
                break
    # 分析msg 回復
    if msg =='幹話':
        print('人只要被殺就會死')
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='人只要被殺就會死\n更多幹話在: https://play.google.com/store/apps/details?id=com.example2.wwesl.fuck_say'))
    elif (msg =="add"):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='添加指令方法:\nadd 你要的指令,你要的回應'))
    elif msg =='A片'or msg =='a片'or  msg =='上車' :
        key_for_18=("Vagina Shaving Tutorial","scannáin","Naked and Funny","18+")
        get_key = random.choices(key_for_18)[0]
        line_bot_api.push_message(source_id,TextSendMessage(text="查詢影片 "+get_key))
        get_youtube(get_key,source_id)
    elif msg =='輔大物理':
        fju_physics(source_id)
    elif "矩陣相乘" in msg:  
        ms = msg.replace("矩陣相乘","")
        get = matrix_dot_func(ms.strip().split("*"))
        line_bot_api.push_message(source_id,TextSendMessage(text=str(get)))
    elif msg =='新聞':
        new_google(source_id)
    elif msg =='指令數量':
        line_bot_api.push_message(source_id,TextSendMessage(text=str(len(all_reply.split('\n'))-1)))
    elif msg[:3] == '歸一化':
        line_bot_api.push_message(source_id,TextSendMessage(text=normolize_volume_integrate(msg.replace('歸一化',''))))
    elif msg[:3] == '體積分':
        line_bot_api.push_message(source_id,TextSendMessage(text=volume_integrate(msg.replace('體積分',''))))
    elif  msg=='新增吃飯':
        line_bot_api.push_message(source_id,TextSendMessage(text='指令用法: 新增吃飯 要加的餐廳'))
    elif msg[:4]=='新增吃飯':
        rest = msg.replace('新增吃飯','')
        add_msg(rest.strip(),eat_name)
        line_bot_api.push_message(source_id,TextSendMessage(text='以新增'+rest))
    elif msg =='吃飯':
        line_bot_api.push_message(source_id,TextSendMessage(text=str(eat(eat_name))))
    elif msg =='積分':
        line_bot_api.push_message(source_id,TextSendMessage(text="指令: 積分,方程式,上界,下界 (目前只能對x積分)"))
    elif '太空' in msg:
        line_bot_api.push_message(source_id,TextSendMessage(text=people_in_space()))
    elif msg[:2] =='積分':
        try:
            if (',' in msg):
                msg = msg.replace('積分,','')
                gg = msg.split(',')
            elif ('，'in msg):
                msg = msg.replace('積分，','')
                gg = msg.split('，')
            print(gg)
            if (len(gg)==3):
                get = integrate_(gg[0].lower(),gg[1],gg[2])
            else:
                get = integrate_(gg[0].lower())
            line_bot_api.push_message(source_id,TextSendMessage(text=get))
        except  Exception as e:
            print(e)
            line_bot_api.push_message(source_id,TextSendMessage(text='無法計算'))
    elif msg =='微分':   
        line_bot_api.push_message(source_id,TextSendMessage(text="指令: 微分,方程式,次數 (目前只能對x微分)"))
    elif msg[:2] =='微分':
        try:
            if (',' in msg):
                msg = msg.replace('微分,','')
                gg = msg.split(',')
            elif ('，'in msg):
                msg = msg.replace('微分，','')
                gg = msg.split('，')
            print(gg)
            if (len(gg)==2):
                get = diffff(gg[0].lower(),gg[1])
            else:
                get = diffff(gg[0].lower())
            line_bot_api.push_message(source_id,TextSendMessage(text=get))
        except:
            line_bot_api.push_message(source_id,TextSendMessage(text='無法計算'))
    elif '降雨' in msg : 
        rain = rain_fall()
        line_bot_api.push_message(source_id,TextSendMessage(text=rain))
    elif 'qrcode' == msg[:6].lower():
        msg = msg[:6].lower() + msg[6:]
        try:
            msg = msg.replace("qrcode","")
            make_Qrcode(msg)
            time.sleep(1)
            try:
                url = get_img('D:/python/linebot/linebot/code.png')
                line_bot_api.push_message(source_id,ImageSendMessage(
                    original_content_url=url,
                    preview_image_url=url
                ))
            except:
                pass
        except:
            line_bot_api.push_message(source_id,TextSendMessage(text="無法製作Qrcode(可能含有中文字)"))
    elif "神的語言" == msg:
        url = god()
        line_bot_api.push_message(source_id,TextSendMessage(text=str(url)))
        try:
            url = get_img('D:/python/linebot/linebot/url_screen.png')
            line_bot_api.push_message(source_id,ImageSendMessage(
                original_content_url=url,
                preview_image_url=url
            ))
        except:
            pass
    elif '神的語言' in msg:
        msg = msg.replace('神的語言','')
        msg = msg.replace(' ','')
        line_bot_api.push_message(source_id,TextSendMessage(text='https://nhentai.net/g/'+ str(msg)))
        try:
            get_screen_url('https://nhentai.net/g/{}'.format(str(msg)))
            time.sleep(1)
            url = get_img('D:/python/linebot/linebot/url_screen.png')
            line_bot_api.push_message(source_id,ImageSendMessage(
                original_content_url=url,
                preview_image_url=url
            ))
        except:
            pass
    #https://nhentai.net/g/
    elif '天氣' in msg:
        get_txt = weather()
        line_bot_api.push_message(source_id,TextSendMessage(text=get_txt))
    elif msg =='溫度':
        line_bot_api.push_message(source_id,TextSendMessage(text=now_weather()))
    elif 'http' in msg[0:4]:
        try:
            get_screen_url(str(msg))
            time.sleep(2)
            url = get_img('D:/python/linebot/linebot/url_screen.png')
            line_bot_api.push_message(source_id,ImageSendMessage(
                original_content_url= url,
                preview_image_url= url
            ))
        except Exception as e:
            print(e)
    elif '地震' in msg :#earthquake()
        line_bot_api.push_message(source_id,TextSendMessage(text='最近發生的地震:\n'+earthquake()))
    elif (msg =="回覆" and user_id == maker):
        ids = get_id_list()
        for i in ids:
            line_bot_api.push_message(maker,TextSendMessage(text=i))
    elif (msg[0:2] =="訊息" and user_id == maker and Permission == 0):
        try:
            id_to = msg.split(' ')[1]
            print(msg.split(' '))
            line_bot_api.push_message(id_to,TextSendMessage(text=  msg.split(' ')[2]))
            line_bot_api.push_message(maker,TextSendMessage(text="傳送成功"))       
        except:
            line_bot_api.push_message(maker,TextSendMessage(text="傳送失敗"))
    elif (msg =='img' and user_id == maker):
        cap = cv2.VideoCapture(0)
        ret,gray = cap.read()
        cv2.imwrite('in.jpg',gray)
        #file:///D:/python/linebot/linebot/in.jpg4
        url = get_img('D:/python/linebot/linebot/in.jpg')
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url=url,
    preview_image_url=url
))
        line_bot_api.push_message(maker,TextSendMessage(text=user_id[:7]+"使用照相功能"))
        line_bot_api.push_message(maker,ImageSendMessage(
    original_content_url=url,
    preview_image_url=url
))
    elif msg =='screen' and (user_id == maker or user_id == girl):
        get_screen = grab_screen()
        cv2.imwrite('screen.jpg',get_screen)
        url = get_img('D:/python/linebot/linebot/screen.jpg')
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(
    original_content_url=url,
    preview_image_url=url
))
        line_bot_api.push_message(maker,TextSendMessage(text=user_id[:7]+"使用截圖功能"))
        line_bot_api.push_message(maker,ImageSendMessage(
    original_content_url=url,
    preview_image_url=url
))
    elif msg[0:4] == '平方數鏈':
##        thread_2 = threading.Thread(target = partial(send_square,msg,send_square))
##        thread_2.daemon = True
##        thread_2.start()
        line_bot_api.push_message(
        source_id,TextSendMessage(
            text="計算中..."
            ))
        try:
            threadgg_2 = threading.Thread(target = partial(square_problem,source_id,msg),name="平方數鏈")
            threadgg_2.daemon = True
            threadgg_2.start()
        except:
            pass
    elif msg[-4:] =='.jpg':
        go_search_google(source_id,msg)
    elif '查詢影片' in msg:
        msg = msg.replace("查詢影片","")
        get_youtube(msg,source_id)
    elif '色情' in msg:
        msg = msg.replace("色情","")
        get_youtube(msg,source_id,porn=True)
    elif 'google' == msg[0:6].lower():
        msg = msg.replace("google","")
        get_google(msg,source_id)
    elif msg =='指令':
        for i,j in reply_dict.items():
            reply_mesg =reply_mesg + i+'\n'
        reply_mesg = reply_mesg + all_reply
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=reply_mesg))
    elif (msg[:3]=="add"):
        ret = msg.replace('add','').strip()
        try:    
            ret = ret.replace('，',',')
            print(ret)
        except:
            pass
        if (Permission == 0):
            filename = "add.txt"
        else:
            filename = "add_2.txt"
        if (not os.path.isfile(filename)):
            with open(filename,'w') as f:
                pass
        with open(filename,'a') as f:
            try:
                f.write(ret+'\n')
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='已添加指令:\n'+ret))
                line_bot_api.push_message(maker,TextSendMessage(text="新的指令被  "+source_id[0:7]+".... 添加了!!"))
                line_bot_api.push_message(maker,TextSendMessage(text=ret))
            except:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text='添加指令:\n'+ret+'\n失敗!!!!!!\n可能有不可讀的文字'))
                line_bot_api.push_message(maker,TextSendMessage(text="新的指令被  "+source_id[0:7]+".... 添加了!!"))
                line_bot_api.push_message(maker,TextSendMessage(text='添加指令:\n'+ret+'\n失敗!!!!!!'))
                
    elif (msg in reply_dict):
        print(reply_dict[msg])
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=(reply_dict[msg])))
        line_bot_api.push_message(source_id, StickerSendMessage(
                    package_id='11538',
                    sticker_id='51626521'
                    ))
    elif '手語' in msg:
        msg = msg.replace('手語','')
        get_msg = hand_lang(msg)
        if (len(get_msg)>1800):
            for i in range(0,len(get_msg),1800):
                line_bot_api.push_message(source_id,TextSendMessage(text=get_msg[0+i,1800+i]))
        else:
            line_bot_api.push_message(source_id,TextSendMessage(text=get_msg))
    elif '翻譯' in msg:
        msg = msg.replace('翻譯','')
        for f in range(0,len(msg),4000): 
            ge = chinese_translate(msg[f +0:f+4000])
            if (len(ge)>1800):
                for i in range(0,len(ge),1800):
                    line_bot_api.push_message(source_id,TextSendMessage(text=ge[0+i,1800+i]))
            else:
                line_bot_api.push_message(source_id,TextSendMessage(text=ge))
                url = get_img('D:/python/linebot/linebot/translate.png')
                line_bot_api.push_message(source_id,ImageSendMessage(
                        original_content_url=url,
                        preview_image_url=url
                    ))
    elif msg == 'start' and Permission == 0:
        thread1 = threading.Thread(target = partial(goodmornig),name ="鬧鐘")
        thread1.daemon = True
        thread1.start()
    elif 'trivago' in msg.lower():
        msg = '''你有在網上找過飯店嗎？
有注意到同一個房間
在不同網站上的價格
可能不一樣嗎？
Trivago幫您即時從250多個訂房網站及app上
比較超過100萬間飯店。
你不要再花大把時間搜尋
最後又做冤大頭。
Trivago幫您又快又簡單的找到理想飯店
讓您輕鬆省荷包。
上Trivago
輸入你要去的地方
選擇入住 退房日期
然後按下搜尋
就是這麼簡單。
點一下
Trivago立即搜尋數百個app及網站。
並秀給您時下最夯的飯店。
你還可以依照自己的預算設定價格範圍
選擇想要入住幾星級的飯店
或是按照我們在線上搜集超過十億條的住客評分來篩選。
記得喔
Trivago顯示的都是同一個房間 不同的報價。
不用懷疑
你可以用Trivago輕輕鬆鬆以划算的價格訂到你理想的住宿。
trivago飯店搜尋讓用戶透過簡單點選
從200多個飯店預訂網站及超過190個國家的130萬家飯店中找到最優惠的飯店報價
我們的網站每年有14億瀏覽次數
旅客固定透過飯店比價來搜尋並比較同一城市的飯店價格
您可以在trivago上獲取週末短程旅遊的資訊
如東京 或大阪
又簡單又迅速就可以找到適合您的飯店
您同樣也可以找適合旅行一周或以上的城市
如紐約及其周邊的飯店
使用trivago您可以簡簡單單的找到理想飯店的最低房價
您只需要輸入您想去的地方和旅遊日期
我們的搜尋引擎就會立刻幫您列出飯店清單並比較所有訂房網站提供的報價
您還可以透過價格 距離（如：離海灘多遠） 星級和飯店設施等等多種篩選條件來客製化您的搜尋結果
您可以透過trivago查找台灣國內各大城市及國外各個熱門旅遊景點的飯店價格
從經濟型旅館到豪華大飯店
trivago讓您的線上訂房程序更加簡單輕鬆!
您可以搜尋台灣各大城市的飯店
如台北
同時也可以搜尋熱門的國外旅遊飯店
如倫敦
我們蒐集了超過2.5億條飯店評價和超過1,900萬張照片
讓您更快的進一步瞭解您旅行目的地的概況
trivago為您提供各飯店的整體評分還有來自國內外各大訂房網站的相關評論
如 Hotels. com Expedia HotelCombined等等
trivago幫您輕鬆地搜尋週末小旅遊的相關資訊
如香港 包括您理想的飯店
trivago是一個飯店比價搜尋引擎
上面的價格都是來自與trivago合作的各大訂房網站以及飯店
當您在trivago上找到了理想的飯店選擇後
透過點選“查看詳情” 您將被引導到該訂房網站
您的訂房手續將在該訂房網站上完成
讓trivago幫您從超過 200 家訂房網站上找到最好康的優惠價格吧
找飯店？Trivago！
'''
        print(msg)
        line_bot_api.push_message(source_id,TextSendMessage(text=str(msg)))
    elif msg == '人數':
        nmu = len(get_id_list())
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="目前我一共有"+str(nmu)+"個聊天室可以聊天"))
    elif msg == '程序':
        for i in threading.enumerate():
            print(i)
            line_bot_api.push_message(source_id,TextSendMessage(text=str(i)))
    elif msg == '開車':
        line_bot_api.push_message(source_id,TextSendMessage(text="關鍵字:  A片, 色情 關鍵字"))
    elif msg == '聊天數據' and Permission == 0:
        if Permission == 0:
            file_name = 'message_collect.txt'
        else:
            file_name = 'message_collect_out.txt'
        with open(file_name,'r') as f:
            gain = f.read()
            get = len(gain)
            t = 0
            line_bot_api.push_message(maker,TextSendMessage(text=source_id+"\n獲取了你的聊天數據"))
            for  i in range(0,get,1800):
                line_bot_api.push_message(source_id,TextSendMessage(text=gain[0+i:1800+i]))
    elif msg == '數據大小':
        if Permission == 0:
            file_name = 'message_collect.txt'
        else:
            file_name = 'message_collect_out.txt'
        with open(file_name,'rb') as f:
            gain = f.read()
            state = len(gain)/1024
            line_bot_api.push_message(source_id,TextSendMessage(text="目前數據大小: {:.2f}kb".format(state)))
    elif '倒水問題' in msg:
        try:
            msg=msg.replace(',',' ')
        except:
            pass
        try:
            msg=msg.replace('，',' ')
        except:
            pass
        ne = msg.split(' ')
        try:
            threadgg_2 = threading.Thread(target = partial(water_problem,source_id,ne),name="倒水問題")
            threadgg_2.daemon = True
            threadgg_2.start()
        except:
            pass
    elif '自言自語' in msg and Permission == 0:
        t = msg.split(' ')
        try:
            threadgg = threading.Thread(target = partial(talk_it_self,source_id,eval(t[1]),t[2]),name="自言自語")
            threadgg.daemon = True
            threadgg.start()
        except:
            pass
    elif '這是' in msg:
        if (',' in msg):
            sp_str = msg.split(',')
            print(sp_str)
            next_msg = sp_str[1]
            msg_2 = sp_str[0]
        elif ('，' in msg):
            sp_str = msg.split('，')
            print(sp_str)
            next_msg = sp_str[1]
            msg_2 = sp_str[0]
        else:
            try:
                msg_2 = msg
                next_msg = msg.replace("這是","",1)
                next_msg = next_msg.replace("嗎","",1)
                next_msg = next_msg.replace("?","",1)
            except:
                pass
        try:
            threadgg = threading.Thread(target = partial(make_butterfly,next_msg,msg_2,source_id),name="梗圖製作")
            threadgg.daemon = True
            threadgg.start()
        except:
            pass
    else:
        if ( Permission == 0):
            file_name = 'message_collect.txt'
        else:
            file_name = 'message_collect_out.txt'
        thread1 = threading.Thread(target = partial(add_msg,msg,file_name),name="添加對話資料庫")
        thread1.daemon = True
        thread1.start()
        try:
            with open(file_name,'r') as f:
                get = f.read()
                ger_sp = get.split('\n')
                flag=0
                this_reply=[]
                for i,j in enumerate(ger_sp):
                    if(msg == j):
                        this_reply.append(ger_sp[i+1])
                        flag = 1
                if (flag == 0):
                    #line_bot_api.reply_message(event.reply_token,TextSendMessage(text='-u-'))
                    pass
                else:
                    reply_random = random.choices(this_reply)[0]
                    print(' 從{}個可能中選擇 --> "{}" 回應'.format(len(set(this_reply)), reply_random))
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=str(reply_random)))
##                    line_bot_api.push_message(source_id, StickerSendMessage(
##                    package_id='11538',
##                    sticker_id='51626521'
##                    ))
        except:
            pass
def new_google(source_id):
    global url_max,lib_you
    url_max , ms = news()
    lib_you.update(
        {source_id:url_max}
        )
    line_bot_api.push_message(source_id,TextSendMessage(
                text=str(ms)))
def people_in_space():
    try:
        import wget
        url = ("http://api.open-notify.org/astros.json")
        filename = wget.download(url,out="rawdata.txt")
        with open("rawdata.txt",'r') as f:
            get = eval(f.read())
            out = '目前太空上的人: {}\n'.format(get['number'])
            for num,name in enumerate(get['people']):
                out =out + '{}. {} ， {}\n'.format(num+1,name['name'],name['craft'])
        print(out)
        os.remove("rawdata.txt")
    except:
        pass
    return out
def fju_physics(source_id):
    global url_max,lib_you
    url_max , ms = fju()
    lib_you.update(
        {source_id:url_max}
        )
    line_bot_api.push_message(source_id,TextSendMessage(
                text=str(ms)))
def get_google(key,source_id):
    global url_max,lib_you
    url_max , ms = get_google_search(key)
    lib_you.update(
        {source_id:url_max}
        )
    line_bot_api.push_message(source_id,TextSendMessage(
                text=str(ms)))
    
def get_youtube(key,source_id,porn=False):
    global url_max,lib_you
    if (porn):
        url_max , ms = search_porn(key)
    else:
        url_max , ms = seaech_google(key)
    lib_you.update(
        {source_id:url_max}
        )
    line_bot_api.push_message(source_id,TextSendMessage(
                text=str(ms)))
def make_butterfly(key,msg,source_id):
    try:
        name = "cover"
        image_name = "cover.png"
        if ('url=' in key):   
            download_url(name,key.strip().replace('url=',''))
        elif ("re" in key):
            image_name = "out.jpg"
        else:
            download(name,key)

        image = cv2.imread("butterfly.png")
        img_PIL = Image.fromarray(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
        font = ImageFont.truetype('DroidSansFallback.ttf', 30)
        fillColor = (255,255,255)
        position = (150,250)
        #msg = msg.encode('utf8')
        draw = ImageDraw.Draw(img_PIL)
        draw.text(position, msg, font=font, fill=fillColor)
        image = cv2.cvtColor(np.asarray(img_PIL),cv2.COLOR_RGB2BGR)
        
        add_image =  cv2.imread(image_name)
        add_image=cv2.resize(add_image,(80,80),interpolation=cv2.INTER_CUBIC)
        x_offset = 300
        y_offset = 35
        image[y_offset:y_offset+add_image.shape[0], x_offset:x_offset+add_image.shape[1]] = add_image
        cv2.imwrite("out.jpg", image)
        url = get_img('D:/python/linebot/linebot/out.jpg')
        line_bot_api.push_message(source_id,ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    ))
    except Exception as e:
        line_bot_api.push_message(source_id,TextSendMessage(
                text="出錯了OAO"+str(e)))
def eat(eat_name):
    if (os.path.isfile(eat_name)):
        with open(eat_name,'r') as f:
            get = f.read().split('\n')
        food = random.choices(get)
        print(food[0])
    else:
        with open(eat_name,'w') as f:
            pass
    return food[0]
def go_search_google(source_id,msg):
    msg = msg.replace('.jpg','')
    image_name = "search.png"
    download("search",msg,0)
    url = get_img('D:/python/linebot/linebot/search.png')
    line_bot_api.push_message(source_id,ImageSendMessage(
        original_content_url=url,
        preview_image_url=url
    ))
def square_problem(source_id,msg):
    out = square_sums_row(int(msg.strip().replace("平方數鏈",'')))
    print(out)
    str_out = str(out)
    for i in range(0,len(str_out),1800):
        line_bot_api.push_message(
            source_id,TextSendMessage(
                text=str_out[0+i:1800+i])
                )
def water_problem(source_id,ne):
    start_time = time.time()
    out=[]
    for i in ne[1:]:
        out.append(eval(i))
    boo, ans = start(out)
    if (boo):
        line_bot_api.push_message(source_id,TextSendMessage(text=ans))
        print("計算時間{:.4f}秒".format(time.time() - start_time))
        line_bot_api.push_message(source_id,TextSendMessage(text="我很厲害喔，只花了{:.4f}秒算出那鬼東西!!".format(time.time() - start_time)))
    elif (ans=='N'):
        line_bot_api.push_message(source_id,TextSendMessage(text="抱歉我的大腦不夠大，算不出來OAQ"))
    else:
        line_bot_api.push_message(source_id,TextSendMessage(text="無解OAO"))
    
def talk_it_self(source_id,left,first):
    if (left ==0):
        return
    try:
        file_name = 'message_collect.txt'
        with open(file_name,'r') as f:
            get = f.read()
            ger_sp = get.split('\n')
            flag=0
            this_reply=[]
            for i,j in enumerate(ger_sp):
                if(first == j):
                    this_reply.append(ger_sp[i+1])
                    flag = 1
            if (flag == 0):
                line_bot_api.push_message(source_id,TextSendMessage(text=str('我沒話說了OAOOO')))
            else:
                reply_random = random.choices(this_reply)[0]
                print('自言自語第{}次'.format(left),reply_random,'"回應\n')
                if (left%2==0):
                    line_bot_api.push_message(source_id,TextSendMessage(text=str('doggy:  '+reply_random)))
                else:
                    line_bot_api.push_message(source_id,TextSendMessage(text=str('mimi:  '+reply_random)))
                time.sleep(0.5)
    except:
        pass
    finally:
        talk_it_self(source_id,left-1,reply_random)
def add_idlist(user_id,file_name): # 新增沒出現過的ID
    if os.path.isfile(file_name): # 如果檔案存在
        with open(file_name,'r') as f: # 用 r 模式 ( read ) 打開
            id_list = f.read().split('\n') 
            if (user_id not in id_list):  # 如果 user_id 不再裡面 則新增
                with open(file_name,'a') as f:  # 用 a 模式 ( append ) 打開
                    f.write(user_id+'\n') # 寫入
                    
                    ############## 跟我說有新的使用者 ##################
                    maker = 'U3e4eca507a83989c933d200b5ec0228a'
                    line_bot_api.push_message(maker,TextSendMessage(text="新的使用者:"+user_id))
                    line_bot_api.push_message(user_id,TextSendMessage(text="歡迎新成員~~"))
                    line_bot_api.push_message(user_id, StickerSendMessage(
                    package_id='11539',
                    sticker_id='52114131'))
                    ###########################################
                    
    else:    # 如果檔案不存在    
        with open(file_name,'w') as f:# 用 w 模式 ( write ) 打開
            f.write(user_id+'\n')
def get_id_list():
    file_name = 'list_id.txt'
    if os.path.isfile(file_name):
        with open(file_name,'r') as f:
            id_list = f.read().split('\n')
    file_name = 'list_id_2.txt'
    if os.path.isfile(file_name):
        with open(file_name,'r') as f:
            id_list_2 = f.read().split('\n')
        return id_list[0:len(id_list)-1]+id_list_2[0:len(id_list_2)-1]
def goodmornig():
    try:
        maker = 'U3e4eca507a83989c933d200b5ec0228a'
        line_bot_api.push_message(maker,TextSendMessage(text="開始每日定時提醒"))
        while 1:
            now_hour = int(datetime.datetime.now().strftime("%H"))
            now_min = int(  datetime.datetime.now().strftime("%M"))
            want_time=(now_hour,now_min)
            to = get_id_list()
            if(now_hour == 8):
                for i in to:
                    line_bot_api.push_message(i,TextSendMessage(text="早安阿~"))
                    line_bot_api.push_message(i, StickerSendMessage(
                        package_id='1',
                        sticker_id='1'
                        ))
                time.sleep(3600)
            elif(now_hour == 0):
                for i in to:
                    line_bot_api.push_message(i,TextSendMessage(text="晚安阿~"))
                    line_bot_api.push_message(i, StickerSendMessage(
                        package_id='1',
                        sticker_id='1'
                        ))
                time.sleep(3600)
            elif (now_hour == 12 and now_min == 50 or now_hour == 8 and now_min == 50 or want_time==(12,59)  or want_time==(8,59)):
                for i in to:
                    line_bot_api.push_message(i,TextSendMessage(text="記得搖蝦幣喔~~"))
                    line_bot_api.push_message(i, StickerSendMessage(
                        package_id='1',
                        sticker_id='2'
                        ))
                time.sleep(120)
            if(False):
                for i in to:
                    line_bot_api.push_message(i,TextSendMessage(text="此為測試訊息，請無視"))
                    line_bot_api.push_message(i, StickerSendMessage(
                        package_id='11538',
                        sticker_id='51626521'
                        ))
                time.sleep(3600)
            time.sleep(60)
    except Exception as e:
        print(e)
        pass
def send_square(msg,id_):
    line_bot_api.push_message(
        id_,TextSendMessage(
            text=str( square_sums_row(int(msg.strip().replace("平方數鏈",''))) )
            ))
def add_msg(msg,file_name):
    if (os.path.isfile(file_name)):
        with open(file_name,'a') as f:
            f.write(msg+'\n')
    else:
        with open(file_name,'w') as f:
            f.write(msg+'\n')
            
def get_img(path):
    global pin
    client = ImgurClient(client_id, client_secret,'61c2a536adcd40eeedbd8e6fba18999f413bf5dc',
                         'aee3d76d7956080282f5d272f76ef12f19509a47')
##    if pin == None:
##        authorization_url = client.get_auth_url('pin')
##        print("Go to the following URL: {0}".format(authorization_url))
##        pin = input("Enter pin code: ")
##    else:
##        pass
##    credentials = client.authorize(pin, 'pin')
##    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    # Example request
    album_id = '2hzdSFn'
    config = {
            'album': album_id,
            'name': 'test-name!',
            'title': 'test-title',
            'description': 'test-description'
            }
    print(client.get_album(album_id))
    client.upload_from_path(path,config=config,anon=False)
    images = client.get_album_images(album_id)
    url = images[len(images)-1].link
    return url


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=False)
