# leetcode 39. 组合总和

class Solution:
    def combinationSum(self, candidates, target):
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
 
    def DFS(self, candidates, target, start, valuelist):
        if target ==  0:
            return Solution.anslist.append(valuelist)
        for i in range(start, len(candidates)):
            #注意在我们的递归函数中，target是不断在变化的
            #因为每次我们调用递归都要用target减去candidates[i],所以这时候如果不保证target比较大，这一定不符合我们的要求
            if candidates[i] > target:
                return
            #递归时我们的减少的条件是target，每次它都会减少
            #如何做到题目说的一个数字可以多次取呢？
            #我们设置了一个start，它会保存上一次取的i,这一次可以继续取，如果符合条件的话
            self.DFS(candidates, target-candidates[i], i, valuelist+[candidates[i]])
                    
