class Solution:
    def hammingWeight(self, n: int) -> int:      
        result=""
        while n>0:
            rem=str(n%2)
            result=rem+result
            n//=2
        count=result.count('1')
        return count
        """return bin(n).count('1')"""

       