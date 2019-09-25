from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urllib.request import urlretrieve
import urllib.request
import requests

from bs4 import BeautifulSoup
import time
import random
import pandas
import jieba
def god():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(firefox_profile = profile)
    while 1:
        num = random.randint(10000,999999)
        url = 'https://nhentai.net/g/'+ str(num)
        driver.get(url)
        driver.maximize_window()
        time.sleep(1)
        try:
            title = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/h1').text
            print(title)
            if (title.strip()!=""):
                driver.save_screenshot('url_screen.png')
                print('yes')
                driver.close()
                driver.quit()
                return 'https://nhentai.net/g/'+ str(num)
                break
        except:
            pass
            
def hand_lang(msg):
    url= 'http://140.123.46.77/TSL/'
    msg = msg.replace(' ','')
    if (',' in msg):
        msg = msg.replace(',','')
    if ('，' in msg):
        msg = msg.replace('，','')
    jjj = jieba.cut(msg)
    
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(firefox_profile = profile)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    input_msg = driver.find_element_by_xpath('//*[@id="searchBar"]')#//*[@id="searchBar"]
    delete = 0
    out = ''
    for item in jjj:
        input_msg.send_keys((delete+3)* Keys.BACKSPACE)
        input_msg.send_keys(item)
        delete = len(item)
        time.sleep(0.1)
        driver.find_element_by_xpath('//*[@id="send"]').click()
        time.sleep(1)
        if (driver.find_element_by_xpath('//*[@id="videoCon"]').text.strip() ==''):
            out = out +item+':\t'+ '請改試較常用的字詞' +'\n\n'
            print(item+':\t'+ '請改試較常用的字詞' +'\n')
        else:
            out = out + item+':\t' + driver.find_element_by_xpath('//*[@id="videoCon"]').text+'\n\n'
            print(item+':\t' + driver.find_element_by_xpath('//*[@id="videoCon"]').text+'\n')       
        time.sleep(1)
    driver.close()
    driver.quit()
    return out
def chinese_translate(be_trans):
    url = 'https://translate.google.com.tw/?hl=zh-TW'
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(firefox_profile = profile)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    input_level = driver.find_element_by_xpath('//*[@id="source"]')
    input_level.send_keys(str(be_trans))
    time_ = len(be_trans)//300 + 1
    time.sleep(time_)
    get_trans = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]').text
    print(get_trans)
    driver.save_screenshot('translate.png')
    driver.close()
    driver.quit()
    return get_trans
    
def rain_fall():
    url = 'https://www.cwb.gov.tw/V7/forecast/taiwan/Taipei_City.htm'
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(firefox_profile = profile)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    get_data = driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div/div[2]/div[2]/table/tbody').text
    msg = '   時間           溫度     降雨幾率\n'
    for i in get_data.split('\n'):
        get = i.split(' ')
        print(get)
        msg = msg + '{:7}'.format(''.join(get[0])) + '{:9}  '.format(' '.join(get[4:7]))+ '{:11}'.format(' '.join(get[8:10])) + '\n'
    print(msg)
    driver.close()
    driver.quit()
    return msg
def get_screen_url(url): # https
    print('打開網站:',url)
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    
    driver = webdriver.Firefox(firefox_profile = profile)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    driver.save_screenshot('url_screen.png')
    driver.close()
    driver.quit()
def make_google_search_url(key):
    out = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwi6oN\
z2r8ffAhWEyLwKHTRjCA8Q_AUIDigB&biw=1536&bih=723".format(key)
    return out
def weather():
    url = "https://www.cwb.gov.tw/V7/forecast/week/w11.htm"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('pre')
    for i in items:
        print(i.get_text())
    return i.get_text()
def news():
    url = "https://news.google.com/?hl=zh-TW&gl=TW&ceid=TW:zh-Hant"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('a',href = True)
    out = []
    msg = ""
    ti = 0
    to = 0
    #更多「頭條新聞」內容
    for i in items:
        if (ti  == 0 and i.get_text().strip() == '更多「頭條新聞」內容' ):
            ti=1
        elif (ti == 1 and to<15 and i.get_text().strip()!='' and '查看完整' not in i.get_text().strip()):
            to +=1
            out.append('https://news.google.com' + i['href'])
            msg = msg + str(to)+ '.  '+ i.get_text() + '\n\n'
    msg  = msg + '請輸入數字來獲得連結'
    return out,msg
def now_weather():
    url = "https://www.google.com/search?q=天氣"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    c = soup.find_all("span",class_='wob_t')[0]
    msg = "現在溫度"+c.get_text()
    print(msg)
    return msg
def earthquake():
    url = 'http://scweb.cwb.gov.tw/Page.aspx?'
    #url = 'https://weather.com/zh-TW/weather/hourbyhour/l/Taipei+Taiwan+TWXX0021:1:TW'
    profile = webdriver.FirefoxProfile()
    profile.set_preference("media.volume_scale", "0.0")
    driver = webdriver.Firefox(firefox_profile = profile)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    get_data = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]').text
    adress = driver.find_element_by_xpath( '/html/body/div[1]/div[2]/div/div[2]/div[2]').text
    date = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]').text
    print(get_data)
    driver.close()
    driver.quit()
    return get_data
def fju():
    url = "http://www.phy.fju.edu.tw/zh_tw/news"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('a',class_='i-annc__title')
    out = []
    msg = ""
    ti = 0
    for i in items:
        ur = "http://www.phy.fju.edu.tw"+i['href']
        ti += 1
        msg = msg + str(ti)+ '.  '+ i.get_text() + '\n\n'
        out.append(ur)
    msg  = msg + '請輸入數字來獲得連結'
    return out,msg
        
def download(name,key,num=None):
    url =make_google_search_url(key)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('img')
    if (num == None):
        num = random.randint(0,len(items)-1)
    html = items[num].get('src')
    urlretrieve(html,name+'.png')
    
def download_url(name,url):
    urlretrieve(url,name+'.png')
##    headers = {'User-Agent': 'Mozilla/5.0'}
##    response = requests.get(url,headers = headers)
##    soup = BeautifulSoup(response.content, 'html.parser',from_encoding="iso-8859-1")
##    items = soup.find_all('img')
##    print(items)
##    if (len(items) ==1 ):
##        num = 0
##    elif(len(items) ==0):
##        print("沒找到圖片")
##        return
##    else:
##        num = random.randint(0,len(items)-1)
##    html = requests.get(items[num].get('src'))
##    with open(name+'.png','wb') as file:
##        file.write(html.content)
##        file.flush

def download_video(name,url):
    #url =make_google_search_url(key)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('img')
    print(items)
    num = random.randint(0,len(items)-1)
    html = requests.get(items[num].get('src'))
    with open(name+'.mp4','wb') as file:
        file.write(html.content)
        file.flush
def get_google_search(key,num=20):
    url = "https://www.google.com/search?q=" + key
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('a',class_ = False,href=True)
    ti = 0
    ti_2 = 0
    out = []
    msg_first =''
    msg = ''
    for i in items:
        if ("youtube" in i['href'] or "map" in i['href']
            or "www.google.com/webhp?"in i['href'] or "這裡"== i.get_text().strip()
            or "" == i.get_text().strip()):
            ti+=1
            continue
        ti_2 += 1
        if ("進階搜尋" ==i.get_text().strip() ):
            break
        get_url = "https://www.google.com"+i['href']
        out.append(get_url)
        msg = msg + str(ti_2)+'.  '+i.get_text().strip()+'\n\n'
        print(ti_2,i.get_text().strip())
        
    msg_first = "以忽略{}筆 地圖 及 yt 影片\n\n".format(ti)
    msg = msg_first + msg
    msg = msg +'請輸入你要的網址數字(最大值'+str(len(out)-1)+')'
    return out,msg

def seaech_google(key,num_s = 10):
    url = "https://www.youtube.com/results?search_query="+key
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('a',title=True,href=True)
    t = 0
    out = []
    nu = 0
    msg = ''
    for i in items:
        if (i['title'].strip() != "按評分排序" and t==0):
            continue
        else:
            if (t == 0):
                t = 1
                continue
            
        if (t == 1  and "http" not in i['title'] and "user" not in i['href']):
            if (nu<num_s):
                nu += 1
                ti = i['title']+'\n'
                msg = msg + str(nu)+'.  '+ti.strip()+'\n'
            url  = 'https://youtu.be'+i['href'].replace('watch?v=','')
            
            out.append(url)
    print(msg)
    msg = msg +'請輸入你要的影片數字(最大值'+str(len(out))+')'
    return out,msg

def search_porn(key,num=13):
    url = 'https://www.youporn.com/search/?query='+str(key)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('a',href=True)
    nu = 0
    msg =''
    out=[]
    for i in items:
        if ("watch" in i['href']):
            out.append("https://www.youporn.com"+i['href'])
            nu +=1
            if (nu<num):
                msg = msg + str(nu)+'.  ' + i.get_text().strip() + '\n\n'
    print(msg)
    msg = msg + '請輸入你要的影片數字(最大值'+str(len(out))+')'
    return out,msg
if __name__ =="__main__":

    get_screen_url("http://www.fju.edu.tw/")
    
