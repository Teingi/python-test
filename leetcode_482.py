#leetcode 482. 密钥格式化

class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        result = ''
        count_k = 0
        for letter in reversed(S):
            if letter != '-':
                result += letter.upper()
                count_k += 1
                if count_k == K:
                    result += '-'
                    count_k = 0
        if len(result) != 0 and result[-1] == '-':
            result = result[:-1]
        return result[::-1]
