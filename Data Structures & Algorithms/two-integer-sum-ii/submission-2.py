class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(numbers)):
            result=target-numbers[i]
            if result in dict:
                return [dict[result],i+1]
            dict[numbers[i]]=i+1

        
        