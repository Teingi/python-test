#leetcode第290题：
#给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
#这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split(' ')
        if len(l) != len(pattern):
            return False
        return len(set(zip(pattern,l))) == len(set(pattern)) == len(set(l))
