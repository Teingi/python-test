#leetcode 819. 最常见的单词


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        from collections import Counter
        pattern = "[A-Za-z]+|\$?\d+%?$"
        r = re.findall(pattern,paragraph.lower())
        List = Counter(r).most_common()
        for i in range(len(List)):
            if List[i][0] in banned:
                pass
            else:
                return List[i][0]
