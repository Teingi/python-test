#leetcode 824. 山羊拉丁文


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        List1 = ['a','e','i','o','u','A','E','I','O','U']
        List2 = S.split()
        List3 = []
        res = ''
        for i in range(len(List2)):
            if List2[i][0] in List1:
                List3.append(List2[i]+'ma'+'a'*(i+1))
            elif List2[i][0] not in List1:
                List3.append(List2[i][1:]+List2[i][0]+'ma'+'a'*(i+1))
        res = List3[0]
        for j in range(1,len(List3)):
            res = res + ' ' + List3[j]
        return res
