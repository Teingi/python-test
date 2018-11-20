#leetcode 840. 矩阵中的幻方


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                set0 = {grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],
                        grid[i][j-1],grid[i][j],grid[i][j+1],
                       grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]}
                set1 = {1,2,3,4,5,6,7,8,9}
                S1 = grid[i-1][j]+grid[i+1][j]
                S2 = grid[i-1][j-1]+grid[i+1][j+1]
                S3 = grid[i-1][j+1]+grid[i+1][j-1]
                S4 = grid[i][j-1]+grid[i][j+1]
                if grid[i][j] == 5:
                    if (set0 == set1) and (S1 == S2 == S3 == S4 == 10):
                        res += 1
                else:
                    pass
        return res
