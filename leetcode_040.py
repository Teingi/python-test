# leetcode 40. 组合总和 II 

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        #储存结果
        Solution.anslist = []
        self.DFS(candidates, target, 0, [])
        return Solution.anslist
 
    def DFS(self, candidates, target, i, valuelist):
        if target ==  0 and valuelist not in Solution.anslist:
            return Solution.anslist.append(valuelist)
        for i in range(i, len(candidates)):
            if candidates[i] > target:
                return
            self.DFS(candidates, target-candidates[i], i+1, valuelist+[candidates[i]])
        
