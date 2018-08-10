#leetcode 205. 同构字符串


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
