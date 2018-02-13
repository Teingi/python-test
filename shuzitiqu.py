import re
import collections
 
def getDigiStr(file_path):
    fp = open(file_path, 'r')
    file_text = fp.read()
    digi_str = re.findall(r'\d{9}',file_text,re.MULTILINE)
    fp.close()
    #数字
    #return '\n https://h5.m.taobao.com/need/weex/container.html?_wx_tpl=https://owl.alicdn.com/mupp-dy/develop/taobao/need/weex/bpu/entry.js&_wx_appbar=true&bpuId='.join(digi_str)
    return '  '.join(digi_str)

if __name__ == '__main__':
    print(getDigiStr(r'E:\\个人文件\\6-desktop\\111111.txt'))

