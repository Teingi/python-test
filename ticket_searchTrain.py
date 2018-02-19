
"""
Usage:
    输入要查询的火车类型可以多选（动车d,高铁g,特快t,快速k,直达z）
    输入出发地、目的地、出发日期。
    查询结果以命令行形式自动呈现。

Examples：
    Please input the trainType you want to search :dgz
    Please input the city you want leave :南京
    Please input the city you will arrive :北京
    Please input the date(Example:2017-09-27) :2018-03-01
"""
#coding = utf-8

import json
import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore
from stations import stations

class searchTrain:
    def __init__(self):
        self.trainOption = input('-d动车 -g高铁 -k快速 -t特快 -z直达,Please input the trainType you want to search :')
        self.fromStation = input('Please input the city you want leave :')
        self.toStation = input('Please input the city you will arrive :')
        self.tripDate = input('Please input the date(Example:2017-09-27) :')
        self.headers = {
            "Cookie":"__NRF=74C05F8DA4A54BAD8FE8C1858576401F; JSESSIONID=7F000001F6317B0C83A920B23A62A0D64E27924D83; route=495c805987d0f5c8c84b14f60212447d; BIGipServerotn=602931722.64545.0000; BIGipServerpool_passport=200081930.50215.0000; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5357%u4EAC%2CNJH; _jc_save_fromDate=2017-07-20; _jc_save_toDate=2017-07-18; _jc_save_wfdc_flag=dc",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
            }
        self.available_trains,self.options = self.searchTrain()

    @property
    def trains(self):
        for item in self.available_trains:
            cm = item.split('|')
            train_no = cm[3]
            initial = train_no[0].lower()
            if not self.options or initial in self.options:
                train = [
                train_no,
                '\n'.join([Fore.GREEN + cm[6] + Fore.RESET,
                          Fore.RED + cm[7] + Fore.RESET]),
                '\n'.join([Fore.GREEN + cm[8] + Fore.RESET,
                          Fore.RED + cm[9] + Fore.RESET]),
                cm[10],
                cm[32],
                cm[25],
                cm[31],
                cm[30],
                cm[21],
                cm[23],
                cm[28],
                cm[24],
                cm[29],
                cm[26],
                cm[22]   ]
                yield train

    def pretty_print(self):
        pt = PrettyTable()
        header = '车次 车站 时间 历时 商务座 特等座 一等 二等 高级软卧 软卧 硬卧 软座 硬座 无座 其他'.split()
        pt._set_field_names(header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

    def searchTrain(self):
        arguments = {
        'option':self.trainOption,
        'from':self.fromStation,
        'to':self.toStation,
        'date':self.tripDate
        }
        options = ''.join([item for item in arguments['option']])
        from_station, to_station, date = stations[arguments['from']] , stations[arguments['to']] , arguments['date']
        url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(date,from_station,to_station)
        requests.packages.urllib3.disable_warnings()
        html = requests.get(url,headers = self.headers,verify=False)
        available_trains = html.json()['data']['result']
        return available_trains,options

if __name__ == '__main__':
    while True:
        asd = searchTrain()
        asd.pretty_print()
