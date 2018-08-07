#leetcode 190. 颠倒二进制位

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        Str = bin(n)
        new = Str[2:][::-1] + '0' * (34-len(Str))
        return int(new, 2)
