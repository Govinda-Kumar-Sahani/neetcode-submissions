class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for val in nums:
            dict[val]=1+dict.get(val,0)
        sorted_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(sorted_dict[i][0])
        return result

        