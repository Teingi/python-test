# leetcode 605. 种花问题


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        m,count,num,i=len(flowerbed),0,0,0
        if m==1 and flowerbed[0]==0:
            num += 1
        while i<m:
            if flowerbed[i]==0:
                count += 1
                if (i==1 or i==m-1) and count==2:
                    num += 1
                    count=1
                if count==3:
                    num += 1
                    count=1
            else:
                count=0
            if num>=n:
                return True
            i += 1            
        return False   
