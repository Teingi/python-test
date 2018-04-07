import os
import string
import re
'''
第 0007 题： 有个目录，里面是你自己写过的程序，
统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
os.chdir('E:\\code\\python')

fh=open('doc_dox.py','r', encoding='UTF-8')
read_fh=fh.readlines()
fh.close()
number_code=0
number_empty=0
number_note=0
pattern='.*#' #正则匹配模式

for x in read_fh:
    if '#' in x: #计算注释数目
        if re.findall(pattern,x)[0][:-1].isspace() or re.findall(pattern,x)[0][:-1]=='':
            number_note+=1
        else:
            number_code+=1

    elif x.isspace():
        number_empty+=1
    else:
        number_code+=1
print('code number is %d'%(number_code+number_empty+number_note))
print('empty number is %d'%number_empty)
print('note number is %d'%number_note)
