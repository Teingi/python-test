#leetcode 599. 两个列表的最小索引总和


class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        List = []
        List_min = []
        List_a = list(range(len(list1)))
        List_b = list(range(len(list2)))
        Dic1 = dict(zip(list1, List_a))
        Dic2 = dict(zip(list2, List_b))
        for res in list1:
            if res in list2:
                List.append(res)
                List_min.append((Dic1.get(res))+(Dic2.get(res)))
        Dic3 = dict(zip(List,List_min))
        Min = min(List_min)

        #在字典中通过value 的值返回key值
        def get_keys(d, value):
            return [k for k,v in d.items() if v == value]


        return get_keys(Dic3,Min)
