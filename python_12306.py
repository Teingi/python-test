#12306账号
myuser="xxxxx"
mypasswd="xxxxx"
import urllib.request
import re
import ssl
import urllib.parse
import http.cookiejar
import datetime
import time

#为了防止ssl出现问题，你可以加上下面一行代码
ssl._create_default_https_context = ssl._create_unverified_context
#查票
#常用三字码与站点对应关系,你所订票的站点没在其中的话需要自己查询添加进去
areatocode={"上海":"SHH","北京":"BJP","南京":"NJH","昆山":"KSH","杭州":"HZH","桂林":"GLZ"}
start1=input("请输入起始站:")
#start1="北京"
start=areatocode[start1]
to1=input("请输入到站:")
#to1="上海"
to=areatocode[to1]
isstudent=input("是学生吗？是：1，不是：0")
#isstudent="0"
date=input("请输入要查询的乘车开始日期的年月，如2017-03-05：")
#date="2018-04-13"
if(isstudent=="0"):
    student="ADULT"
else:
    student="0X00"
url="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date="+date+"&\
leftTicketDTO.from_station="+start+"&leftTicketDTO.to_station="+to+"&purpose_codes="+student
context = ssl._create_unverified_context()
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
patrst01='"result":\[(.*?)\]'
rst01=re.compile(patrst01).findall(data)[0]
allcheci=rst01.split(",")
checimap_pat='"map":({.*?})'
checimap=eval(re.compile(checimap_pat).findall(data)[0])
print("车次\t出发站名\t到达站名\t出发时间\t到达时间\t一等座\t二等座\t硬座\t无座")
for i in range(0,len(allcheci)):
    try:
        thischeci=allcheci[i].split("|")
        #[3]---code
        code=thischeci[3]
        #[6]---fromname
        fromname=thischeci[6]
        fromname=checimap[fromname]
        #[7]---toname
        toname=thischeci[7]
        toname=checimap[toname]
        #[8]---stime
        stime=thischeci[8]
        #[9]---atime
        atime=thischeci[9]
        #[28]---yz
        yz=thischeci[31]
        #[29]---wz
        wz=thischeci[30]
        #[30]---ze
        ze=thischeci[29]
        #[31]---zy
        zy=thischeci[26]
        print(code+"\t"+fromname+"\t"+toname+"\t"+stime+"\t"+atime+"\t"+str(zy)+"\t"+str(ze)+"\t\
              "+str(yz)+"\t"+str(wz))
    except Exception as err:
        pass
isdo=input("查票完成，请输入1继续…")
#isdo=1
if(isdo==1 or isdo=="1"):
    pass
else:
    raise Exception("输入不是1，结束执行")
print("Cookie处理中…")
#以下进行登陆操作
#建立cookie处理
cjar=http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
#以下进入自动登录部分
loginurl="https://kyfw.12306.cn/otn/login/init#"
req0 = urllib.request.Request(loginurl)
req0.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req0data=urllib.request.urlopen(req0).read().decode("utf-8","ignore")
 
yzmurl="https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
while True:
    urllib.request.urlretrieve(yzmurl,"./12306_yzm.png")
    yzm=input("请输入验证码，输入第几张图片即可")#需要输入""
    if(yzm!="re"):
        break
#x坐标(35,112,173,253)，y坐标(45)
#x坐标(35,112,173,253)，y坐标(114)
pat1='"(.*?)"'
allpic=re.compile(pat1).findall(yzm)
def getxy(pic):
    if(pic==1):
        xy=(35,45)
    if(pic==2):
        xy=(112,45)
    if(pic==3):
        xy=(173,45)
    if(pic==4):
        xy=(253,45)        
    if(pic==5):
        xy=(35,114)
    if(pic==6):
        xy=(112,114)
    if(pic==7):
        xy=(173,114)
    if(pic==8):
        xy=(253,114)
    return xy
allpicpos=""
for i in allpic:
    thisxy=getxy(int(i))
    for j in thisxy:
        allpicpos=allpicpos+str(j)+","
allpicpos2=re.compile("(.*?).$").findall(allpicpos)[0]
print(allpicpos2)
#post验证码验证
yzmposturl="https://kyfw.12306.cn/passport/captcha/captcha-check"
yzmpostdata =urllib.parse.urlencode({
"answer":allpicpos2,
"rand":"sjrand",
"login_site":"E",
}).encode('utf-8')
req1 = urllib.request.Request(yzmposturl,yzmpostdata)
req1.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req1data=urllib.request.urlopen(req1).read().decode("utf-8","ignore")
#post账号密码验证
loginposturl="https://kyfw.12306.cn/passport/web/login"
loginpostdata =urllib.parse.urlencode({
"username":myuser,
"password":mypasswd,
"appid":"otn",
}).encode('utf-8')
req2 = urllib.request.Request(loginposturl,loginpostdata)
req2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req2data=urllib.request.urlopen(req2).read().decode("utf-8","ignore")
#其他验证
loginposturl2="https://kyfw.12306.cn/otn/login/userLogin"
loginpostdata2 =urllib.parse.urlencode({
"_json_att":"",
}).encode('utf-8')
req2_2 = urllib.request.Request(loginposturl2,loginpostdata2)
req2_2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req2data_2=urllib.request.urlopen(req2_2).read().decode("utf-8","ignore")
 
loginposturl3="https://kyfw.12306.cn/passport/web/auth/uamtk"
loginpostdata3 =urllib.parse.urlencode({
"appid":"otn",
}).encode('utf-8')
req2_3 = urllib.request.Request(loginposturl3,loginpostdata3)
req2_3.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req2data_3=urllib.request.urlopen(req2_3).read().decode("utf-8","ignore")
pat_req2='"newapptk":"(.*?)"'
tk=re.compile(pat_req2,re.S).findall(req2data_3)[0]
 
loginposturl4="https://kyfw.12306.cn/otn/uamauthclient"
loginpostdata4 =urllib.parse.urlencode({
"tk":tk,
}).encode('utf-8')
req2_4 = urllib.request.Request(loginposturl4,loginpostdata4)
req2_4.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req2data_4=urllib.request.urlopen(req2_4).read().decode("utf-8","ignore")
#爬个人中心页面
centerurl="https://kyfw.12306.cn/otn/index/initMy12306"
req3 = urllib.request.Request(centerurl)
req3.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lik\
e Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
req3data=urllib.request.urlopen(req3).read().decode("utf-8","ignore")
print("登陆完成")
#isdo="1"
isdo=input("如果需要订票，请输入1继续，否则请输入其他数据")
if(isdo==1 or isdo=="1"):
    pass
else:
    raise Exception("输入不是1，结束执行")
thiscode=input("请输入要预定的车次：")
chooseno="None"
#chooseno="1"
while True:
    try:
        #订票
        #先初始化一下订票界面
        initurl="https://kyfw.12306.cn/otn/leftTicket/init"
        reqinit=urllib.request.Request(initurl)
        reqinit.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        initdata=urllib.request.urlopen(reqinit).read().decode("utf-8","ignore")
        #再爬对应订票信息
        bookurl="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date="+date+"&leftTi\
cketDTO.from_station="+start+"&leftTicketDTO.to_station="+to+"&purpose_codes="+student
        req4 = urllib.request.Request(bookurl)
        req4.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHT\
ML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req4data=urllib.request.urlopen(req4).read().decode("utf-8","ignore")
        #存储车次与secretStr信息
        patrst01='"result":\[(.*?)\]'
        rst01=re.compile(patrst01).findall(req4data)[0]
        allcheci=rst01.split(",")
        checimap_pat='"map":({.*?})'
        checimap=eval(re.compile(checimap_pat).findall(req4data)[0])
        code=[]
        secretStr=[]
        zy=[]
        for i in range(0,len(allcheci)):
            try:
                thischeci=allcheci[i].split("|")
                #print(thischeci)
                #[3]---code
                thiscode1=thischeci[3]
                code.append(thiscode1)
                #[0]---secretStr
                secretStr.append(thischeci[0].replace('"',""))
                #[31]-zy
                thiszy=thischeci[31]
                zy.append(thiszy)
            except Exception as err:
                pass
        #用字典trainzy存储车次有没有票的信息
        trainzy={}
        for i in range(0,len(code)):
            trainzy[code[i]]=zy[i]
        #用字典traindata存储车次secretStr信息，以供后续订票操作
        #存储的格式是：traindata={"车次1":secretStr1,"车次2":secretStr2,…}
        traindata={}
        for i in range(0,len(code)):
            traindata[code[i]]=secretStr[i]
        #订票-第1次post-主要进行确认用户状态
        checkurl="https://kyfw.12306.cn/otn/login/checkUser"
        checkdata =urllib.parse.urlencode({
        "_json_att":""
        }).encode('utf-8')
        req5 = urllib.request.Request(checkurl,checkdata)
        req5.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req5data=urllib.request.urlopen(req5).read().decode("utf-8","ignore")
        #自动得到当前时间并转为年-月-格式，因为后面请求数据需要用到当前时间作为返程时间backdate
        backdate=datetime.datetime.now()
        backdate=backdate.strftime("%Y-%m-%d")
        #订票-第2次post-主要进行“预订”提交
        submiturl="https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest"
        submitdata =urllib.parse.urlencode({
        "secretStr":traindata[thiscode],
        "train_date":date,
        "back_train_date":backdate,
        "tour_flag":"dc",
        "purpose_codes":student,
        "query_from_station_name":start1,
        "query_to_station_name":to1,
        })
        submitdata2=submitdata.replace("%25","%")
        submitdata3=submitdata2.encode('utf-8')
        req6 = urllib.request.Request(submiturl,submitdata3)
        req6.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req6data=urllib.request.urlopen(req6).read().decode("utf-8","ignore")
        #订票-第3次post-主要获取Token、leftTicketStr、key_check_isChange、train_location
        initdcurl="https://kyfw.12306.cn/otn/confirmPassenger/initDc"
        initdcdata =urllib.parse.urlencode({
        "_json_att":""
        }).encode('utf-8')
        req7 = urllib.request.Request(initdcurl,initdcdata)
        req7.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req7data=urllib.request.urlopen(req7).read().decode("utf-8","ignore")
        #获取train_no、leftTicketStr、fromStationTelecode、toStationTelecode、train_location
        train_no_pat="'train_no':'(.*?)'"
        leftTicketStr_pat="'leftTicketStr':'(.*?)'"
        fromStationTelecode_pat="from_station_telecode':'(.*?)'"
        toStationTelecode_pat="'to_station_telecode':'(.*?)'"
        train_location_pat="'train_location':'(.*?)'"
        pattoken="var globalRepeatSubmitToken.*?'(.*?)'"
        patkey="'key_check_isChange':'(.*?)'"
        train_no_all=re.compile(train_no_pat).findall(req7data)
        if(len(train_no_all)!=0):
            train_no=train_no_all[0]
        else:
            raise Exception("train_no获取失败")
        leftTicketStr_all=re.compile(leftTicketStr_pat).findall(req7data)
        if(len(leftTicketStr_all)!=0):
            leftTicketStr=leftTicketStr_all[0]
        else:
            raise Exception("leftTicketStr获取失败")
        fromStationTelecode_all=re.compile(fromStationTelecode_pat).findall(req7data)
        if(len(fromStationTelecode_all)!=0):
            fromStationTelecode=fromStationTelecode_all[0]
        else:
            raise Exception("fromStationTelecod获取失败")
        toStationTelecode_all=re.compile(toStationTelecode_pat).findall(req7data)
        if(len(toStationTelecode_all)!=0):
            toStationTelecode=toStationTelecode_all[0]
        else:
            raise Exception("toStationTelecode获取失败")
        train_location_all=re.compile(train_location_pat).findall(req7data)
        if(len(train_location_all)!=0):
            train_location=train_location_all[0]
        else:
            raise Exception("train_location获取失败")
        tokenall=re.compile(pattoken).findall(req7data)
        if(len(tokenall)!=0):
            token=tokenall[0]
        else:
            raise Exception("Token获取失败")
        keyall=re.compile(patkey).findall(req7data)
        if(len(keyall)!=0):
            key=keyall[0]
        else:
            raise Exception("key_check_isChange获取失败")
        #还需要获取train_location
        pattrain_location="'tour_flag':'dc','train_location':'(.*?)'"
        train_locationall=re.compile(pattrain_location).findall(req7data)
        if(len(train_locationall)!=0):
            train_location=train_locationall[0]
        else:
            raise Exception("train_location获取失败")
        #自动post网址4-获取乘客信息
        getuserurl="https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs"
        getuserdata =urllib.parse.urlencode({
        "REPEAT_SUBMIT_TOKEN":token,
        }).encode('utf-8')
        req8 = urllib.request.Request(getuserurl,getuserdata)
        req8.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req8data=urllib.request.urlopen(req8).read().decode("utf-8","ignore")
        #获取用户信息
        #提取姓名
        namepat='"passenger_name":"(.*?)"'
        #提取身份证
        idpat='"passenger_id_no":"(.*?)"'
        #提取手机号
        mobilepat='"mobile_no":"(.*?)"'
        #提取对应乘客所在的国家
        countrypat='"country_code":"(.*?)"'
        nameall=re.compile(namepat).findall(req8data)
        idall=re.compile(idpat).findall(req8data)
        mobileall=re.compile(mobilepat).findall(req8data)
        countryall=re.compile(countrypat).findall(req8data)
        #选择乘客
        if(chooseno!="None"):
            pass
        else:
            #输出乘客信息，由于可能有多位乘客，所以通过循环输出
            for i in range(0,len(nameall)):
                print("第"+str(i+1)+"位用户,姓名:"+str(nameall[i]))
            chooseno=input("请选择要订票的用户的序号，此处只能选择一位哦，如需选择多\
位，可以自行修改一下代码")
            #thisno为对应乘客的下标，比序号少1，比如序号为1的乘客在列表中的下标为0
            thisno=int(chooseno)-1
        if(trainzy[thiscode]=="无"):
            print("当前无票，继续监控…")
            continue
        #总请求1-点击提交后步骤1-确认订单(在此只定二等座，座位类型为1，如需选择多种类型座位，可
        #以自行修改一下代码使用if判断一下即可)
        checkOrderurl="https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo"
        checkdata=urllib.parse.urlencode({
        "cancel_flag":2,
        "bed_level_order_num":"000000000000000000000000000000",
        "passengerTicketStr":"M,0,1,"+str(nameall[thisno])+",1,"+str(idall[thisno])+",\
"+str(mobileall[thisno])+",N",
        "oldPassengerStr":str(nameall[thisno])+",1,"+str(idall[thisno])+",1_",
        "tour_flag":"dc",
        "randCode":"",
        "whatsSelect":1,
        "_json_att":"",
        "REPEAT_SUBMIT_TOKEN":token,
        }).encode('utf-8')
        req9 = urllib.request.Request(checkOrderurl,checkdata)
        req9.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KH\
TML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req9data=urllib.request.urlopen(req9).read().decode("utf-8","ignore")
        print("确认订单完成，即将进行下一步")
        #总请求2-点击提交后步骤2-获取队列
        getqueurl="https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount"
        #checkdata=checkOrderdata.encode('utf-8')
        #将日期转为格林时间
        #先将字符串转为常规时间格式
        thisdatestr=date#需要的买票时间
        thisdate=datetime.datetime.strptime(thisdatestr,"%Y-%m-%d").date()
        #再转为对应的格林时间
        gmt='%a+%b+%d+%Y'
        thisgmtdate=thisdate.strftime(gmt)
        #将leftstr2转成指定格式
        leftstr2=leftTicketStr.replace("%","%25")
        getquedata="train_date="+str(thisgmtdate)+"+00%3A00%3A00+GMT%2B0800&train_no="+train_no+"&sta\
tionTrainCode="+thiscode+"&seatType=M&fromStationTelecode="+fromStationTelecode+"&toStationTelecod\
e="+toStationTelecode+"&leftTicket="+leftstr2+"&purpose_codes=00&train_location="+train_location+"&_j\
son_att=&REPEAT_SUBMIT_TOKEN="+str(token)
        getdata=getquedata.encode('utf-8')
        req10 = urllib.request.Request(getqueurl,getdata)
        req10.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTM\
L, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req10data=urllib.request.urlopen(req10).read().decode("utf-8","ignore")
        print("获取订单队列完成，即将进行下一步")
        #总请求3-确认步骤1-配置确认提交
        confurl="https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue"
        confdata2=urllib.parse.urlencode({
        "passengerTicketStr":"M,0,1,"+str(nameall[thisno])+",1,"+str(idall[thisno])+",\
"+str(mobileall[thisno])+",N",
        "oldPassengerStr":str(nameall[thisno])+",1,"+str(idall[thisno])+",1_",
        "randCode":"",
        "purpose_codes":"00",
        "key_check_isChange":key,
        "leftTicketStr":leftTicketStr,
        "train_location":train_location,
        "choose_seats":"",
        "seatDetailType":"000",
        "whatsSelect":"1",
        "roomType":"00",
        "dwAll":"N",
        "_json_att":"",
        "REPEAT_SUBMIT_TOKEN":token,
        }).encode('utf-8')
        req11 = urllib.request.Request(confurl,confdata2)
        req11.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.3\
6 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req11data=urllib.request.urlopen(req11).read().decode("utf-8","ignore")
        print("配置确认提交完成，即将进行下一步")
        time1=time.time()
        while True:
            #总请求4-确认步骤2-获取orderid
            time2=time.time()
            if((time2-time1)//60>5):
                print("获取orderid超时，正在进行新一次抢购")
                break
            getorderidurl="https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random="+str(int(time.time()*1000))+"&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN="+str(token)
            req12 = urllib.request.Request(getorderidurl)
            req12.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
            req12data=urllib.request.urlopen(req12).read().decode("utf-8","ignore")
            patorderid='"orderId":"(.*?)"'
            orderidall=re.compile(patorderid).findall(req12data)
            if(len(orderidall)==0):
                print("未获取到orderid，正在进行新一次的请求。")
                continue
            else:
                orderid=orderidall[0]
                break
        print("获取orderid完成，即将进行下一步")
        #总请求5-确认步骤3-请求结果
        resulturl="https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue"
        resultdata="orderSequence_no="+orderid+"&_json_att=&REPEAT_SUBMIT_TOKEN="+str(token)
        resultdata2=resultdata.encode('utf-8')
        req13 = urllib.request.Request(resulturl,resultdata2)
        req13.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
        req13data=urllib.request.urlopen(req13).read().decode("utf-8","ignore")
        print("请求结果完成，即将进行下一步")
        try:
            #总请求6-确认步骤4-支付接口页面
            payurl="https://kyfw.12306.cn/otn//payOrder/init"
            paydata="_json_att=&REPEAT_SUBMIT_TOKEN="+str(token)
            paydata2=paydata.encode('utf-8')
            req14 = urllib.request.Request(payurl,paydata2)
            req14.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')
            req14data=urllib.request.urlopen(req14).read().decode("utf-8","ignore")
            print("订单已经完成提交，您可以登录后台进行支付了。")
            break
        except Exception as err:
            break
    except Exception as err:
        print(err)
