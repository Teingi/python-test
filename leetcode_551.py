#leetcode 551. 学生出勤纪录 I


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        List_A = []
        List_L = []
        for i in range(len(s)):
            if s[i] == 'A':
                List_A.append(i)
            elif s[i] == 'L':
                List_L.append(i)
            else:
                pass
        if len(List_A) >= 2:
            return False
        elif len(List_A) < 2 and len(List_L) <= 2:
            return True
        else:
            res = 2
            while (List_L[res-2 : res+1] != [List_L[res-2],List_L[res-2]+1,List_L[res-2]+2]) and (res <= len(List_L)-1): 
                res = res + 1
            if res < len(List_L):
                return False
            else:
                return True
