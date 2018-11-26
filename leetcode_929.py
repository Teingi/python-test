#leetcode 929. 独特的电子邮件地址


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = []
        for email in emails:
            result.append(self.newEmail(email))
        return len(set(result))
        
        
    def newEmail(self,email):
        '''
        按规则转换之后的emali
        '''
        a = email.index('+')
        b = email.index('@')
        List = email[:a].split('.')
        res_s = ''
        for s in List:
            res_s += s
        return res_s + email[b:]
