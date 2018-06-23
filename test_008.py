import json  
import xlwt  
from collections import OrderedDict
'''
city.txt
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}


####################
numbers.txt
[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]

######################
student.txt
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}


'''  
  
def run_1():  
  
    with open('E:\\code\\student.txt','r') as f:  
        content = f.read()  
  
    #转化为json，注意转化后的dict的元素位置可能和转化前可能不一样，因此需要ordereddict  
    #loads()方法把str对象反序列化为json对象，自定义解码器为ordereddict  
    d = json.loads(content,object_pairs_hook=OrderedDict)  
    print(d)  
    #初始化xls文件  
    file = xlwt.Workbook()  
    #添加sheet,工作表，名字为test  
    table = file.add_sheet('test')  
    for row ,i in enumerate(d):   #读取所有字典，row为序号，i为字典关键字key  
        table.write(row,0,i)    #写入（行号，列号，key)  
        for col,j in enumerate(d[i]):   #col为序号，j为value,有多个，需要迭代  
            table.write(row,col+1,j)  
  
    file.save('E:\\code\\student.xls')  
  
  
  
def run_2():  
    with open('E:\\code\\city.txt','r') as f:  
        content = f.read()  
    #同上  
    d = json.loads(content,object_pairs_hook=OrderedDict)  
    file = xlwt.Workbook()  
    table = file.add_sheet('rest')  
    for row ,i in enumerate(d):  
        table.write(row,0,i)  
        table.write(row,1,d[i])  
    file.save('E:\\code\\city.xls')  
  
  
def run_3():  
    with open('E:\\code\\numbers.txt','r') as f:  
        content = f.read()  
  
    d = json.loads(content,object_pairs_hook=OrderedDict)  
    file = xlwt.Workbook()  
  
    table = file .add_sheet('test')  
    for row , i in enumerate(d):  
        for col, j in enumerate(i):  
            table.write(row,col,j)  
  
    file.save('E:\\code\\number.xls')  
  
  
if __name__ =="__main__":  
    run_1()  
    run_2()  
    run_3()  
