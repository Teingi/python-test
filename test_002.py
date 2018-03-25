#encoding=utf-8


#随机生成一个字符串
'''
import random
import string
number = int(input('验证码位数：'))

def gene_text():
    source_num = ['0','1','2','3','4','5','6','7','8','9']
    source_string = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J', 'K','L', 'M', 'N','O','P','Q','R',
              'S', 'T', 'U', 'V', 'W', 'Z','X', 'Y']
    x = ''.join(random.sample(source_num,number))
    y = ''.join(random.sample(source_string,number))
    return (x, y)#number是生成验证码的位数

yzm = gene_text()
print(yzm)

'''
import random
def gen_code(length=8):  
    """ 
    将0~9,a~z,A~Z保存到list中，用random.sample从list中取固定位数 
    """  
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

for num in range(0,200):
    print(gen_code())
    
    
