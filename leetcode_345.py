#leetcode 345
#编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

class Solution(object):
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
    	sl = list(s)
    	begin = 0
    	end = len(s) - 1
    	while begin < end:
        	while begin < end and sl[begin].lower() not in vowels:
        		begin += 1;
       		while begin < end and sl[end].lower() not in vowels:
        		end -= 1;
        	sl[begin],sl[end] = sl[end],sl[begin];
        	begin += 1;
        	end -= 1;
        return ''.join(sl)
