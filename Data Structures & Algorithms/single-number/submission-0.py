class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for val in nums:
            dict[val]=1+dict.get(val,0)
        for key,value in dict.items():
            if value==1:
                return key
        