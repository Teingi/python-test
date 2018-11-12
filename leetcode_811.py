#leetcode 811. 子域名访问计数


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        temp = {}
        for i in range(len(cpdomains)):
            c = cpdomains[i].split()
            r = ''
            for j in range(len(c[1].split('.'))-1,-1,-1):
                r = '.'+ c[1].split('.')[j] + r
                if r.lstrip('.') in temp:
                    temp[r.lstrip('.')] += int(c[0])
                else:
                    temp[r.lstrip('.')] = int(c[0])
        return ["%d %s" % (temp[k], k) for k in temp]
