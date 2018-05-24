# -*- coding: UTF-8 -*-

'''
罗马数字转整数
'''

s = input("请输入一个罗马数字：")
#D = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

def Trans(lm):
    D = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum1 = 0
    i = 0
    for i in range(0,int(len(lm))):
        if(i < len(lm)-1):
            if D[lm[i]] > D[lm[i+1]]:
                sum1 += D[lm[i]]
                #i=i+1
            elif D[lm[i]] < D[lm[i+1]]:
                if lm[i] == 'C' and lm[i+1] == 'M':
                    sum1 += 900
                 #   i=i+1
                elif lm[i] == 'C' and lm[i+1] == 'D':
                    sum1 += 400
                  #  i=i+1
                elif lm[i] == 'X' and lm[i+1] == 'C':
                    sum1 += 90
                   # i=i+1
                elif lm[i] == 'X' and lm[i+1] == 'L':
                    sum1 += 40
                    #i=i+1
                elif lm[i] == 'I' and lm[i+1] == 'X':
                    sum1 += 9
                    #i=i+1
                elif lm[i] == 'I' and lm[i+1] == 'V':
                    sum1 += 4
                    #i=i+1
                else:
                    #print("输入不符合规范！！！")
                    break
            else:
                sum1 = sum1 + D[lm[i]]
                #i=i+1
        else:
            sum1 = sum1 + D[lm[i]]
                
    return sum1

num = Trans(s)

if num > 0:
    print("对应的阿拉伯数字是：",num)
else:
    print("输入不符合规范！！！")
                
                
        

        
