# -*- coding:utf-8 -*-

"""
给定一个字符串所表示的括号序列，包含以下字符：
'(', ')', '{', '}', '[' and ']'
判定是否是有效的括号序列。

"""

strs = list(input("请输入括号序列："))
#print(strs)

def isValid(s):
    if s is None:return False
    str_x = ["(","[","{"]
    str_y = [")","]","}"]
    str_z = ["()","[]","{}"]

    res = []
    for i in s:
        if i in str_x:
            res.append(i)
        elif i in str_y:
            if res == []:
                return False
            else:
                temp = res.pop(-1) + i
                if temp not in str_z:
                    return False
    if len(res) != 0:
        return False
    return True
    

print(isValid(strs))

            
            





        
        
    
