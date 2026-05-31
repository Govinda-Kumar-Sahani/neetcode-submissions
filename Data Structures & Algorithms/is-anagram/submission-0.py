class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_str1=sorted(s)
        sorted_str2=sorted(t)
        if sorted_str1==sorted_str2:
            return True
        else:
            return False
        