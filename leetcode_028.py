# -*- coding:utf-8 -*-


'''
给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
如果不存在，则返回  -1

'''
haystack_raw= input("请输入haystack 字符串：")
needle_raw = input("请输入needle 字符串：")


def strStr(haystack,needle):
    if len(needle) == 0:
        return 0
    else:
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] ==needle:
                return i
        return -1

strS = strStr(haystack_raw,needle_raw)
print(strS)
                    
