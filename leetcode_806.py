#leetcode 806. 写字符串需要的行数

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        res = [1,0]
        S_raw = "abcdefghijklmnopqrstuvwxyz"
        raw_num = 0
        for s in S:
            s_index = S_raw.index(s)
            raw_num += widths[s_index]
            if raw_num > 100:
                res[0] += 1
                raw_num = widths[s_index]
        res[1] = raw_num
        return res
