from functools import cache
from typing import List


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         @cache
#         def canFinish(idx):
#             if idx == len(nums)-1:
#                 return True
#             if idx>=len(nums):
#                 return False
            
#             # 0 is only tolerable in the last position, but if we are already in the last position first condition
#             # will trigger
#             if nums[idx] == 0:
#                 return False
            
#             for t in range(nums[idx], 0, -1):
#                 if idx+t < len(nums) and canFinish(idx+t):
#                     return True
#             return False
        
        
#         return canFinish(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i]>=target:
                target = i
        return target == 0