from typing import List
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        leftMin = [-1]
        rightMin = [-1]
        
        # print(nums)
        curMin = nums[0]
        for i in range(1, len(nums)):
            leftMin.append(curMin)
            curMin = min(curMin, nums[i])
        
        # print(leftMin)
        
        curMin = nums[-1]
        for i in range(len(nums)-2, -1,-1):
            rightMin.append(curMin)
            curMin = min(curMin, nums[i])
        
        rightMin.reverse()
        # print(rightMin)
        
        
        ansfound = False
        res = sum(nums)
        
        for i in range(1, len(nums)-1):
            lmin = leftMin[i]
            rmin = rightMin[i]
            cur = nums[i]
            
            if lmin<cur>rmin:
                ansfound = True
                res = min(res, lmin+cur+rmin)
        
        if ansfound:
            return res
        return -1
            
        

s = Solution()

print(s.minimumSum([8,6,1,5,3]))
        