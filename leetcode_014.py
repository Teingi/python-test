# -*- coding:UTF-8 -*-

'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

'''

string_add = input("输入字符串，以空格切分:")
string = string_add.split(' ')
# print(string)

#匹配最长相同字符
def longestCommonPrefix(strs):
    if len(strs)==0:
        return ''
        
    elif len(strs)==1:
        return strs[0]
    else:
        b=sorted(strs,key=lambda x:len(x))
        s=''
        s1=b[0]
        for i,v in enumerate(s1):
            l = []
            for j in b[1:]:
                l.append(v==j[i])
            if all(l):
                s+=v
            else:
                break
        return s



st = longestCommonPrefix(string)
if st == '':
    print("没有匹配选项！！")
else:
    print("最长匹配字符为：",st)
