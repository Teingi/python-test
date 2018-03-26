#encoding=utf-8

#coding: utf-8
#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
from random import choice
import string
import pymysql.cursors

#随机生成一个字符串
"""
import random
import pymysql
def gen_code(length=8):  

    #将0~9,a~z,A~Z保存到list中，用random.sample从list中取固定位数
 
    code_list = []  
    for i in range(10):  
        code_list.append(str(i))  
        #print i  
    for i in range(65, 91):  
        code_list.append(chr(i))  
        #print chr(i)  
    for i in range(97, 123):  
        code_list.append(chr(i))  
  
    myslice = random.sample(code_list, length)  
    veri_code = ''.join(myslice)  
    return veri_code

#打印生成的200个验证码
for num in range(0,200):
    print(gen_code())

print("哈哈哈哈")
m = gen_code()
print(m)

#存储到mysql数据库中
    
# 打开数据库连接
db = pymysql.connect("localhost",'root','123456','python_db')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS GENCODE")

# 使用预处理语句创建表
sql_new = "CREATE TABLE GENCODE (m varchar(8))"

cursor.execute(sql_new)

# SQL 插入语句
sql_expend = "INSERT INTO GENCODE(m),VALUES('%s')" %(m)
cursor = db.cursor()

try:
   # 执行sql语句
   cursor.execute(sql_expend)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()
"""


def get_code(dict, length, count):
#根据给定字典，长度来得出激活码
    for i in range(1,int(count)+1):
        code = ""
    #通过count限制激活码个数，循环调用choice来计算激活码
        for l in range(0,int(length)):
            code = code+str(choice(dict))
        save_to_mysql(i, code)

def save_to_mysql(id, code):
#保存到mysql数据库
    #设置数据库连接相关信息
    # connect = pymysql.connect(host, user, pass_, db)
    connect = pymysql.connect("localhost",'root','123456','python_db')
    cursor = connect.cursor()
    # sql_new = "CREATE TABLE GENCODE (id int,code varchar(8))"
    # cursor.execute(sql_new)
    #链接数据库并设置游标
    sql = "insert into GENCODE(id, code) VALUES ('%d', '%s')"
    data = (id, code)
    cursor.execute(sql % data)
    #执行sql语句

if __name__ == "__main__":
    dict = string.ascii_letters[:]
    #设定字典为'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = input("请输入激活码个数：")
    if count == "":
        count = "1"
    length = input("请输入激活码长度：")
    if length == "":
        length = "8"
    get_code(dict, length, count)

