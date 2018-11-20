#leetcode 844. 比较含退格的字符串


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.backspaceString(S) == self.backspaceString(T)
        
        
    def backspaceString(self,Str):
        '''
        求退格后的字符串函数
        '''
        List = []
        for i in range(len(Str)):
            if Str[i] != '#':
                List.append(Str[i])
            elif Str[i] == '#' and len(List) != 0:
                List.pop()
        return List
