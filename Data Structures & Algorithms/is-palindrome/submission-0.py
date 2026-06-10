class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for ch in s:
            if ch.isalnum():
                string+=ch.lower()
        if string==string[::-1]:
            return True
        else:
            return False
                
        