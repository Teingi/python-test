# leetcode 682. 棒球比赛


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        b=[1 for i in range(len(ops))]
        for i in range(len(ops)):
            if ops[i]=="C" :
                b[i]=0
                j=i
                while b[j]==0:
                    j=j-1
                b[j]=0
            if ops[i] == "D":
                j=i-1
                while b[j]==0:
                    j=j-1
                ops[i]=2*int(ops[j])
            if ops[i]=="+":
                j = i - 1
                while b[j] == 0:
                    j = j - 1
                k=j-1
                while b[k] == 0:
                    k = k - 1
                ops[i]=int(ops[j])+int(ops[k])
        sum=0
        for i in range(len(ops)):
            if b[i]==1:sum=sum+int(ops[i])
        return sum
