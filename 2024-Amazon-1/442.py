from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # res = []
        # i = 0
        # while i < len(nums):
        #     cur = nums[i]
        #     cursPos = cur - 1
        #     if i != cursPos and cur != -1: # make sure we are not self looping over the position
        #         if nums[cursPos] == cur: # so we found a duplicate
        #             nums[i] = -1 # mark as duplicate
        #             res.append(cur)
        #             i+=1
        #         else:
        #             nums[i], nums[cursPos] = nums[cursPos], nums[i]
        #     else:
        #         i+=1
        # print(nums)
        # return res
        
        res = []
        for n in nums:
            n = abs(n)
            if nums[n-1]<0:
                res.append(n)
                continue
            else:
                nums[n-1] = - nums[n-1]
        
        # print(nums)
        return res

s = Solution()

print(s.findDuplicates(nums = [4,3,2,7,8,2,3,1]))
print(s.findDuplicates(nums = [1,1,2]))
print(s.findDuplicates( nums = [1]))