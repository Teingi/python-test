# leetcode 557. 反转字符串中的单词 III


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        List_s = s.split(' ')
        List_raw = []
        for i in range(len(List_s)):
            List_raw.append(List_s[i][::-1])
        Str =''
        for j in range(len(List_raw)-1):
            Str = Str + str(List_raw[j]) + ' '
        Str = Str + str(List_raw[-1])
        return Str
