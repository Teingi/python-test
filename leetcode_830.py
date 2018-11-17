# leetcode 830. 较大分组的位置


class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        S = S + ' '
        if len(S) < 3:
            return []
        raw = []
        i,j = 0,1
        while (i < j) and (j < len(S)):
            if S[i] == S[j]:
                j += 1                
            else:
                if j >= i + 3:
                    raw.append([i,j-1])
                i = j
                j += 1
        return raw
