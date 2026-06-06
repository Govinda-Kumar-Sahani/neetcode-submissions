class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num=[]
        for i in range(len(nums)):
            result=1
            for j in range(len(nums)):
                if i!=j:
                    result=result*nums[j]
            num.append(result)
        return num
        