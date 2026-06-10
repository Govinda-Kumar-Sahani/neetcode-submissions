class Solution:
    def reverse(self, x: int) -> int:
        result=""
        sign=-1 if x<0 else 1
        a=abs(x)
        while a>0:
            rem=str(a%10)
            result=result+rem
            a//=10
        num=sign*int(result or "0")
        if num<(-2**31) or num>(2**31-1):
            return 0
        return num
        