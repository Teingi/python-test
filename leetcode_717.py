# leetcode 717. 1比特与2比特字符

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits_reverse = bits[::-1]
        bits_reverse.append(0)
        id1 = [i for i,x in enumerate(bits_reverse) if x==0]
        if id1[1] % 2 == 0:
            return False
        else:
            return True
