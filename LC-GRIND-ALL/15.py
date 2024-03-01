from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if i-1>=0 and nums[i-1] == nums[i]: # skip the duplicates
                continue
            ## We do regular two sum here with two pointers
            l,r = i+1, n-1
            while(l<r):
                if nums[l] + nums[r] == -nums[i]:
                    res.append([nums[i], nums[l], nums[r]])
                    t = nums[l]
                    while(l<r and t == nums[l]):
                        l+=1
                    t = nums[r]
                    while(l<r and t == nums[r]):
                        r-=1
                elif nums[l] + nums[r] > -nums[i]:
                    r -=1 
                else:
                    l+=1
        return res