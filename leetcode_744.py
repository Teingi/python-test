# leetcode 744. 寻找比目标字母大的最小字母


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters_sort = sorted(set(letters))
        if target in letters_sort and letters_sort.index(target) < len(letters_sort) - 1:
            return letters_sort[letters_sort.index(target) + 1]
        elif target in letters_sort and letters_sort.index(target) == len(letters_sort) - 1:
            return letters_sort[0]
        elif target not in letters_sort:
            letters_sort.append(target)
            letters_sortNew = sorted(letters_sort)
            if letters_sortNew.index(target) == len(letters_sortNew) - 1:
                return letters_sortNew[0]
            else:
                return letters_sortNew[letters_sortNew.index(target) + 1]



