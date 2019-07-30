# -*- coding: utf-8 -*-
import os, sys
import requests
import re
from bs4 import *

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态码不是200，引发异常
        r.encoding = 'utf-8'
        return r.text
    except:
         return "产生异常"

def getPic(srcList, html):
    try:
        #srcurl = re.findall('https://cbu01.alicdn.com/img/ibank/\d{4}/\d{3}/\d{3}/\d{11}_\d{10}\.220x220xz\.jpg', html)
        #srcurl = re.findall(r'https://cbu01\.alicdn\.com/img/ibank/2019/356/147/11639741653_1496901083\.220x220xz\.jpg', html)
        soup = BeautifulSoup(html, "html.parser")
        all_img = soup.find_all('img')
        for img in all_img:
            srcList.append(img['src'])
    except:
        print ("找不到")


def savePic(picList, root):
    for src in picList:
        path = root + src.split('/')[-1]
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                pic = requests.get(src)
                with open(path, 'wb') as f:
                    f.write(pic.content)
                    f.close()
                    print('success')
            else:
                print('already exist')
        except:
            print('error')

def main():
    depth = 2
    infoList = []
    for i in range(depth):
        try:
             url = 'http://s.1688.com/selloffer/offer_search.htm?keywords=%C4%D0%D7%B0&button_click=top&earseDirect=false&n=y&netType=1%2C11#beginPage={0}&offset=8&filterP4pIds=564572467279,553466615860,598626744329,594640698847,557462306973,597827089274,592049248690'.format(i)
             #print url
             html = getHTMLText(url)
             #print html
             getPic(infoList, html)
        except:
            continue
    root = "/home/acro/Spider/shi"
    savePic(infoList, root)
    #print (infoList)
    #print (len(infoList))




main()