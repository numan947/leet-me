from typing import List
from unittest import result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        taken = [0]*len(nums)
        tmpRes = []
        result = []
        
        def permuteAll():
            if len(tmpRes) == len(nums):
                result.append([x for x in tmpRes])
                return    
            for i in range(len(nums)):
                if taken[i] == 0:
                    taken[i] = 1
                    tmpRes.append(nums[i])
                    permuteAll()
                    taken[i] = 0
                    tmpRes.pop()
        
        permuteAll()
    
        return result

s = Solution()

print(s.permute([1,2]))