#coding = utf-8
import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
requests.packages.urllib3.disable_warnings()#如果不加此句会有：InsecureRequestWarning: Unverified HTTPS request is being made
html = requests.get(url,verify=False)
station = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', html.text)
stations = dict(station)
pprint(stations,indent = 4)
