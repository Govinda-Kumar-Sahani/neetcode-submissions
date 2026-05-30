class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for val in nums:
            if val in dict:
                return True
            else:
                dict[val]=1
        return False
        