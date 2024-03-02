from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        tmpRes = []
        
        def findCandidates(remain, startIdx):
            if remain == 0:
                result.append([x for x in tmpRes])
                return
            if remain<0 or startIdx >= len(candidates):
                return
            
            for i in range(startIdx, len(candidates)):
                tmpRes.append(candidates[i])
                findCandidates(remain-candidates[i], i)
                tmpRes.pop()
        
        findCandidates(target, 0)
        return result


s = Solution()

print(s.combinationSum([3], 8))