from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        
        for s in strs:
            tmp = list(s)
            tmp.sort()
            tmp = ''.join(tmp)
            
            if tmp not in hMap.keys():
                hMap[tmp] = []
            hMap[tmp].append(s)
        
        return hMap.values()