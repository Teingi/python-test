# leetcode 443. 压缩字符串


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i,n=0,len(chars)
        char_str=''
        while i<n:
            count=1
            while i<n-1 and chars[i+1]==chars[i]:
                i += 1
                count += 1
            char_str += chars[i]
            if count>1:
                char_str += str(count)
            i += 1
        char_str=list(char_str)
        for j in range(len(char_str)):
            chars[j]=char_str[j]
        return len(char_str)
