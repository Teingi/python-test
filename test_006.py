#-*-coding=utf-8

# Python小程序练习---敏感词替换成*星号
'''
user_input=input('请评论：')
for filter_word in open('E:\\code\\python\\filtered_words.txt'):
    fw=filter_word.rstrip()
    if fw in user_input:
        fw_len=len(fw)
        user_input=user_input.replace(fw,'*'*fw_len)

else:
    print(user_input)


#! /usr/bin/env python
#! -*- coding: utf-8 -*-


import re
file = open("E:\\code\\python\\filtered_words.txt","r")
list_key_word =[]
try:
    list_key_word = file.readlines()
finally:
    file.close()
for i in range(len(list_key_word)):
    list_key_word[i]=list_key_word[i].strip(" \n")
while(True):
    userinput = input("Please input something.\n")
    result = ""
    for x in list_key_word:
        #result = userinput.replace(x,"*")
        result = re.sub(x,"*",userinput)
        userinput = result
    print(result)
    continue_or_not = input("Do you want continue? Please input y/n. Any other inputs will be taken as y.\n")
    if continue_or_not.lower() == 'n':
        break

# if __name__ == '__main__':
'''
import re


def change_input():
    file = open("E:\\code\\python\\filtered_words.txt","r")
    list_key_word =[]
    try:
        list_key_word = file.readlines()
    finally:
        file.close()
    for i in range(len(list_key_word)):
        list_key_word[i]=list_key_word[i].strip(" \n")
    while(True):
        userinput = input("Please input something.\n")

        # with open("E:\\code\\0.txt","r") as userinput:
        # result = userinput.read()
        result = ""
        for x in list_key_word:
            #result = userinput.replace(x,"*")
            result = re.sub(x,"*",userinput)
            userinput = result
        #print(result)
        with open("E:\\code\\1.txt","a") as f:
            print(result,file = f)
        continue_or_not = input("Do you want continue? Please input y/n. Any other inputs will be taken as y.\n")
        if continue_or_not.lower() == 'n':
            break
change_input()


