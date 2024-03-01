from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenBefore = {}
        
        for i, n in enumerate(nums):
            if (target - n) in seenBefore:
                return [i, seenBefore[target-n]]
            seenBefore[n] = i
        return []