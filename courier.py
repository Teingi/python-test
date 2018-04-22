#-*-coding:utf-8 -*-
# python request模块通过模拟用户访问web网站，实际运用到Html的post，get的方法实现网站互动
import json,requests
def searchPackage():
    #输入运单号码，注意，只有正在途中的快递才可以查到
    packageNum = input('请输入运单号码：')
    url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum
    #用url1查询运单号对应的快递公司，如中通，返回：zhongtong。
    companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
    #在用url2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
    url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum #还有个temp字段加不加都可以。如：'&temp=0.9829438147420106'
    print('时间↓                             地点和跟踪进度↓\n')
    for item in json.loads(requests.get(url2).text)['data']:
        print(item['time'],item['context'])
searchPackage()
