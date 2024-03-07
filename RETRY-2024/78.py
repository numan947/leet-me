from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        tmpRes = []
        def subgen(idx):
            if idx == len(nums):
                res.append([x for x in tmpRes])
                return
            
            tmpRes.append(nums[idx])
            subgen(idx+1)
            tmpRes.pop()
            subgen(idx+1)
        
        subgen(0)
        return res

s = Solution()
print(s.subsets([0]))