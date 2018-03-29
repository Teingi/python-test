'''
import os
from PIL import Image

pathDir='E:\\code\\yzm'
os.chdir(pathDir)

def modify_imgsize():
    for filename in get_imglist():
        img=Image.open(filename)
        if max(img.size)>1024:
            value=max(img.size)/1024.0
            newsize_min=min(img.size)/value
            mewimg = img.resize((1024,int(newsize_min)),Image.ANTIALIAS)#修改大小
        else:
            print("This pictureis available:"+filename)

def get_imglist():
    img_list=[]
    list_dir=os.listdir(pathDir)
    for x in list_dir:
        if '.JPG' in x:
            img_list.append(x)
        else:
            print("This is not a picture:"+x)
    return img_list

modify_imgsize()
'''
from pathlib import Path
from PIL import Image


def modify_imgsize(fileUrl):
    p = Path(fileUrl)
    ImgFileList = list(p.glob('*.JPG'))
    ImgFileList.extend(list(p.glob('*.JPG')))
    for filename in ImgFileList:
        img = Image.open(filename)
        if max(img.size) > 1000:
            value = max(img.size) / 1000.0
            newsize_min = min(img.size) / value
            newimg = img.resize((1000, int(newsize_min)), Image.ANTIALIAS)  # 修改大小
            newimg.save('new_' + filename.name, 'jpeg')
        else:
            print("This picture is availabe:" + filename.name)


if __name__ == '__main__':
    modify_imgsize('E:\\code\\yzm')
