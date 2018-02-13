#-*-coding:utf-8 -*-
import urllib.request  
from time import ctime
from bs4 import BeautifulSoup
import itchat
def getPM25(cityname):
    site = 'http://www.pm25.com/' + cityname + '.html'
    page = urllib.request.urlopen(site)
    html = page.read();
    soup = BeautifulSoup(html.decode("utf-8"),"html.parser")
    city = soup.find(class_='bi_loaction_city')  # 城市名称
    aqi = soup.find("a", {"class", "bi_aqiarea_num"})  # AQI指数
    quality = soup.select(".bi_aqiarea_right span")  # 空气质量等级
    result = soup.find("div", class_='bi_aqiarea_bottom')  # 空气质量描述
    output=city.text + u'AQI指数：' + aqi.text + u'\n空气质量：' + quality[0].text + result.text
    print(output)
    print('*' * 20 + ctime() + '*' * 20)
    return output
itchat.auto_login(hotReload=True)
Help="""
友情提示：
请输入城市拼音获取天气结果，如果无法识别，自动返回首都记录
"""
itchat.send(Help,toUserName='filehelper')
@itchat.msg_register(itchat.content.TEXT)
def getcity(msg):
    if msg['ToUserName'] != 'filehelper': return
    print(msg['Text'])
    cityname=msg['Text']
    result=getPM25(cityname)
    itchat.send(result,'filehelper')
if __name__ == '__main__':
    itchat.run()
