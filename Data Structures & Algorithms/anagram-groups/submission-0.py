class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for char in strs:
            sorted_char=''.join(sorted(char))
            if sorted_char not in dict:
                dict[sorted_char]=[]
            dict[sorted_char].append(char)
        return list(dict.values())
        