#leetcode 728. 自除数

class Solution:
    def selfDividingNumbers(self, left, right):
        def isdivid(num):
            list1 = list(str(num))
            if '0' in list1: return False
            for item in list1:
                if num % int(item) != 0:
                    return False
            return True
        if left > right: return []
        res = []
        for i in range(left,right+1):
            if isdivid(i): res.append(i)
        return res
