# leetcode 500. 键盘行

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        keyset=['qwertyuiop','asdfghjkl','zxcvbnm']
        for keys in keyset:
            for word in words:
                line=set(word.lower())
                if line.issubset(set(keys)):
                    ans.append(word)
        return ans
