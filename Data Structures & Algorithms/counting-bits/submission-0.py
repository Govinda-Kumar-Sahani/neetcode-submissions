class Solution:
    def countBits(self, n: int) -> List[int]:
        num=[]
        for i in range(n+1):
            count=bin(i).count('1')
            num.append(count)
        return num
        