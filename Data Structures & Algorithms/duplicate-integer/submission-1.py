class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for val in nums:
            if val not in dict:
                dict[val]=1
            else:
                return True
        return False
        