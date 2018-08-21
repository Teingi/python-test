#leetcode 657. 判断路线成圈


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        List_R, List_L, List_U, List_D = [], [], [], []
        for i in range(len(moves)):
            if moves[i] == 'R':
                List_R.append(i)
            elif moves[i] == 'L':
                List_L.append(i)
            elif moves[i] == 'U':
                List_U.append(i)
            elif moves[i] == 'D':
                List_D.append(i)
            else:
                pass
        if (len(List_R) == len(List_L)) and (len(List_U) == len(List_D)):
            return True
        else:
            return False
