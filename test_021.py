# coding:UTF-8
import tkinter
import tkinter as tk
import random
x,y,s=0,0,0
z=int(random.random()*1000)
def getx():
    global x,y,s
    s=x+y+1
    if  shuru.get() != '':
        n=int(shuru.get())
        if n>z:
            shuchu['text'] ='你输入的是:',n,',太大了'
            x=x+1
        if n==z:
            shuchu['text']='你输入的是：',n,'恭喜你答对了！你尝试了',s,'次！'
        if n<z:
            shuchu['text']='你输入的是:',n,',太小了'
            y=y+1
root=tk.Tk()
root.title('猜数字游戏')
tk.Label(text='请输入一个数字').pack()
#输入
shuru=tk.Entry() #不能把pack()直接加Entry()后面！！！
shuru.pack()
#按钮
comand = tk.Button(root,text="确定", command=getx)
comand.pack()
#回车

#输出
shuchu=tk.Label(root,text='输出')
shuchu.pack()
#显示
root.mainloop()
