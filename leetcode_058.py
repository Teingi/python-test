# -*- coding: utf-8 -*-


'''
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

'''

s_raw = input("请输入字母和空格组成的字符串：")


#转换字符串为列表
def trans(strs):
    strs_new = strs.split(" ")
    list_str = []
    
    for i in range(len(strs_new)):
        list_str.append(strs_new[i])
    return list_str
       
#返回最后单词的长度
def lengthOfLastWord(s):
	#倒序循环，从最后一个元素循环到第一个元素。不能用正序循环，
    #因为正序循环删除元素后后续的列表的长度和元素下标同时也跟着变了，len(alist)是动态的。
    for j in range(len(s)-1,-1,-1):
        if s[j] == "":
            s.remove("")
            
    print(s)
    if s == []:
        return 0
    else:
        return len(s[-1])


s_new = trans(s_raw)
print(s_new)
s_final = lengthOfLastWord(s_new)
print(s_final)


