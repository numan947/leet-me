from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        tmp = []
        def findcandiates(remain, start):
            if remain == 0:
                res.append(list(tmp))
                return
            
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c<=remain:
                    tmp.append(c)
                    findcandiates(remain-c, i)
                    tmp.pop()
                    
        findcandiates(target, 0)
        return res
                    