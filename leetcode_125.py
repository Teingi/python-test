#leetcode 125. 验证回文串

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        set_num = set('0123456789')
        set_str = set('abcdefghijklmnopqrstuvwxyz')
        List = []
        for i in range(len(s)):
            if (s[i] in set_num) or (s[i].lower() in set_str):
                List.append(s[i].lower())
        if List == List[::-1]:
            return True
        else:
            return False
