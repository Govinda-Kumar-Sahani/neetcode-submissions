class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """sorted_str1=sorted(s)
        sorted_str2=sorted(t)
        if sorted_str1==sorted_str2:
            return True
        else:
            return False"""
        """if len(s)!=len(t):
            return False
        dict1,dict2={},{}
        for i in range(len(s)):
            dict1[s[i]]=1+dict1.get(s[i],0)
            dict2[t[i]]=1+dict2.get(t[i],0)
        return dict1==dict2"""
        return Counter(s)==Counter(t)
        
    
        