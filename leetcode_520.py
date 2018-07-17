# leetcode 520. 检测大写字母

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        str_A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        str_a = 'abcdefghijklmnopqrstuvwxyz'
        if len(word) == 1:
            return True
        else:
            if set(word).issubset(set(str_a)) or set(word).issubset(set(str_A)):
                return True
            elif word[0] in set(str_A) and set(word[1:]).issubset(set(str_a)):
                return True
            else:
                return False
