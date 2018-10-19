'''
import os
files = os.listdir("E:/code/StudentSystem/admin")#获取当前目录下的文件

for filename in files:
    portion = os.path.splitext(filename)#将文件名拆成名字和后缀
    print(portion)
    if portion[1] == ".htm":#关于后缀
        newname = portion[0] + ".html"
        os.rename(filename, newname)#修改
        os.rename(os.path.join("E:/code/StudentSystem/admin",filename),newname) 
'''


##python批量更换后缀名
import os
import sys
path0=r"E:\code\StudentSystem\admin"
path1=r"E:\code\StudentSystem\admin"+'\\'
sys.path.append(path1)
# print(sys.path)
# 列出当前目录下所有的文件
files = os.listdir(path0)
# files = os.listdir('.')
print('files',files)
for filename in files:
  portion = os.path.splitext(filename)
  # 如果后缀是.txt
  if portion[1] == ".htm": 
    # 重新组合文件名和后缀名
    newname = portion[0] + ".html"
    filenamedir=path1 +filename
    newnamedir=path1+newname
    # os.rename(filename,newname)
    os.rename(filenamedir,newnamedir)
