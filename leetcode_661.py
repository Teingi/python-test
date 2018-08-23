
# leetocde 661. 图片平滑器

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        result=[]
        m,n=len(M),len(M[0])
        for i in range(m):
            result.append([])
            for j in range(n):
                value,count=M[i][j],1
                if i-1>=0:
                    value += M[i-1][j]
                    count += 1
                    if j-1>=0:
                        value += M[i-1][j-1]
                        count += 1
                    if j+1<n:
                        value += M[i-1][j+1]
                        count += 1
                if i+1<m:
                    value += M[i+1][j]
                    count += 1
                    if j-1>=0:
                        value += M[i+1][j-1]
                        count += 1
                    if j+1<n:
                        value += M[i+1][j+1]
                        count += 1
                if j-1>=0:
                    value += M[i][j-1]
                    count += 1
                if j+1<n:
                    value += M[i][j+1]
                    count += 1
                result[i].append(value/count)
        return result
