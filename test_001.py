#!/usr/bin/python  
# -*- coding: UTF-8 -*-
# @Author  : Teingi

"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。 类似于图中效果



from PIL import Image,ImageDraw,ImageFont
ttfont = ImageFont.truetype("C:\\Windows\\Fonts\\STXINGKA.TTF",50)
im = Image.open("E:\\code\\python\\test\\day01\\001.jpg")
draw = ImageDraw.Draw(im) 
draw.text((10,10), u'美女', fill=(5,0,0),font=ttfont)
im.show()

"""
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def white_to_transparent(img):
    img=img.convert('RGBA') #返回一个转换后的图像的副本
    datas=img.getdata()
    newData=[]
    for item in datas:
        if item[0]==255 and item[1]==255:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    img.putdata(newData)    #赋给图片新的像素数据
    return img

if __name__=="__main__":

    p1_name="E:\\code\\python\\test\\day01\\001.jpg"
    p2_name="E:\\code\\python\\test\\day01\\002.jpg"
    #打开两张png图片，注意为当前路径
    p1_image=Image.open(p1_name)
    p2_image=Image.open(p2_name)
    p2_transparent=white_to_transparent(p2_image)
    p1_image.paste(p2_transparent,(0,0),p2_transparent)

    usr_font=ImageFont.truetype("C:\\Windows\\Fonts\\STXINGKA.TTF",32)
    draw=ImageDraw.Draw(p1_image) #在p1_image上绘制文字，图像
    draw.text((152,8),u'12',font=usr_font)
    p1_image.save("final.png","PNG")
