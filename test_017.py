#递归实现汉诺塔
#n层汉诺塔最少需要移动 2^n - 1 步
import time
n = int(input("请输入汉诺塔的层数："))

starttime = time.clock()
def hanot(n,x,y,z):
    if n == 1:
        print(x,'--->',z)
    else:
        hanot(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        print(x,'--->',z)#将最底下的最后一个盘子从x移动到z上
        hanot(n-1,y,x,z)#将y上的n-1个盘子移动到z上
hanot(n,'X','Y','Z')
endtime = time.clock()
print(endtime - starttime)
