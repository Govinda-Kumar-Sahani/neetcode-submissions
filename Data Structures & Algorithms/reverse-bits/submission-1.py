class Solution:
    def reverseBits(self, n: int) -> int:
        """ res=0
        for i in range(32):
            bit=(n>>i)&1
            res=res|(bit<<(31-i))
        return res"""
        binary=format(n,'032b')
        reverse=binary[::-1]
        decimal=int(reverse,2)
        return decimal