#bin/sys/python
# --*coding:utf-8*--


import re
import urllib.request

#-----------获取网页源代码的方法------------
def getHtml(url):
	page=urllib.request.urlopen(url)
	html=page.read()
	return html
	
#-------------getHtml()内输入任意帖子的URL----------
html=getHtml("http://tieba.baidu.com/p/3205263090")

#---------------修改html对象的字符编码为UTF-8-------
html=html.decode('UTF-8')

#-----------获取帖子内所有图片的方法---------
def getImg(html):
	#------利用正则表达式匹配网页内容找到图片地址-----
	reg=r'src="([.*\S]*\.jpg)" pic_ext="jpeg"'
	imgre=re.compile(reg);
	imglist=re.findall(imgre,html)
	return imglist

imgList=getImg(html)
imgName=0
for imgPath in imgList:
	#------这里最好使用异常处理及多线程编程方式------------
	f=open("E:\\code\\yzm\\"+str(imgName)+".jpg",'wb')
	f.write((urllib.request.urlopen(imgPath)).read())
	f.close()
	
	imgName += 1
	
print("All Done!")
