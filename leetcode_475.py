
#leetcode 475. 供暖器


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        radius = -sys.maxint - 1
        i, j = 0, 0
        while (i < len(houses)):
            if (j == len(heaters)):
                radius = max(radius, houses[i] - heaters[j - 1])
                i += 1
            elif (houses[i] <= heaters[j]):
                radius = max(radius, heaters[j] - houses[i])
                i += 1
            elif (j == len(heaters) - 1):
                radius = max(radius, houses[i] - heaters[j])
                i += 1
            elif (houses[i] >= heaters[j + 1]):
                j += 1
            else:
                diff = min(houses[i] - heaters[j], heaters[j + 1] - houses[i])
                radius = max(radius, diff)
                i += 1
        return radius
