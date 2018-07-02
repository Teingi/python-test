#leetcode383python赎金信

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True
        dic1=collections.Counter(ransomNote)#制作字典
        dic2=collections.Counter(magazine)
        count=0#记录dic1中满足的字符个数
        for key in dic1.keys():
            if key in dic2.keys():
                if dic1[key]<=dic2[key]:
                    #return True#字典是无序的，所以不能用这个
                    count+=1
        return True if count==len(dic1) else False#个数等于dic的个数则满足
