#leetcode 784. 字母大小写全排列


class Solution(object):
    def spliteList(self, alist):
        flag = 0    # 判断是否还含有两个字母的元素
        for i in range(len(alist)):
            k = alist[i]
            if len(k) == 2:
                flag = 1
                list1 = alist[:i] + [k[0].lower()] + alist[i+1:]
                list2 = alist[:i] + [k[0].upper()] + alist[i+1:]
                break

        if flag == 0:
            return alist
        else:
            return list1, list2


    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        sList = list( S )
        letterNum = 0
        for i in range(len(S)):
            k = sList[i]
            if 'A'<= k <= 'z':
                letterNum += 1  # 统计一下字母的个数
                sList[i] = k.lower() + k.upper()

        allList = []
        allList.append( sList )

        while len( allList ) != 2**letterNum:
            l = len( allList )
            for i in range(l):
                list1 = allList[i]
                if len( list1 ) != len( ''.join(list1)):
                    del allList[i]
                    l1, l2 = self.spliteList( list1 )
                    allList.append( l1 )
                    allList.append( l2 )

        l = len( allList )
        for i in range(l):
            allList[i] = ''.join( allList[i] )

        return allList
