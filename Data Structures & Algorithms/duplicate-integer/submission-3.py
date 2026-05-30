class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """dict={}
        for val in nums:
            if val in dict:
                return True
            else:
                dict[val]=1
        return False"""
        num=sorted(nums)
        for i in range(len(num)-1):
            if num[i]==num[i+1]:
                return True
        return False


        