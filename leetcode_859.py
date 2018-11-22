#leetcode 859. 亲密字符串


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        List = []
        if (set(A) != set(B)) or (len(A) != len(B)):
            return False
        for i in range(len(A)):
            if A[i] != B[i]:
                List.append(i)
        if (len(List) == 0) and (len(set(A)) < len(A)):
            return True
        elif len(List) == 0 and (len(set(A))==len(A)):
            return False
        elif len(List) == 1:
            return False
        elif len(List) == 2 and (A[List[0]]==B[List[1]] and A[List[1]]==B[List[0]]):
            return True
        else:
            return False
