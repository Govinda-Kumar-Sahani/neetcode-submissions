class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest=1
        current=1
        sort=sorted(set(nums))
        for i in range(1,len(sort)):
            if sort[i]==sort[i-1]+1:
                current+=1
            else:
                longest=max(longest,current)
                current=1
        longest=max(longest,current)
        return longest
        