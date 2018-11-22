#leetcode 860. 柠檬水找零


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if len(bills) == 0:
            return True
        List = []
        res = []
        for i in range(len(bills)):
            if bills[i] == 5:
                List.append(5)
            elif bills[i] == 10:
                if (5 in List):
                    List.remove(5)
                    List += [10]
                else:
                    res.append(0)
            elif bills[i] == 20:
                if (5 in List):
                    List.remove(5)
                    if (10 in List):
                        List.remove(10)
                    elif (10 not in List) and (5 in List):
                        List.remove(5)
                        if (5 in List):
                            List.remove(5)
                        else:
                            res.append(0)
                    else:
                        res.append(0)
                else:
                    res.append(0)
            else:
                res.append(0)
        if len(res) >= 1:
            return False
        else:
            return True
