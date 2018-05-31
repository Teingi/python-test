# -*- coding:utf-8 -*-
'''
二进制求和

'''
a_raw = input("请输入二进制数a：")
b_raw = input("请输入二进制数b：")



#将字符串二进制转变为十进制数
def trans(s):
    num = 0
    for i in range(len(s)):
        if s[i] == "0":
            num = num + 0
        elif s[i] == "1":
            num = num + 2**(len(s)-i-1)
        else:
            return -1 
    return num


a_new = trans(a_raw)
b_new = trans(b_raw)

if a_new == -1 or b_new == -1:
    print("输入错误，求和失败：")
else:
    #print(a_new)
    #print(b_new)
    c = a_new + b_new

    #将十进制数转变成2进制并换作字符串
    str_c = str(bin(c))
    #print(str_c)
    str_cnew = str_c[2:]
    print("求和结果是：", str_cnew)

    
    
