#leetcode 3. 无重复字符的最长子串

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record_place = {}
        max_len = 0
        mid_max_len = 0
        for (i, ch) in enumerate(s):
            if ch not in record_place:
                mid_max_len += 1
                if max_len < mid_max_len:
                    max_len = mid_max_len
            else:
                if i - record_place[ch] > mid_max_len:
                    mid_max_len += 1
                    if mid_max_len > max_len:
                        max_len = mid_max_len
                else:
                    mid_max_len = i - record_place[ch]

            record_place[ch] = i
        return max_len
