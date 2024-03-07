from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        pivot = len(nums)-1
        
        while pivot>=0 and nums[pivot]<=(nums[pivot-1]):
            pivot-=1
        
        pivot = pivot-1
        if pivot<0:
            s = 0
            e = len(nums)-1
            while s<e:
                nums[s], nums[e] = nums[e], nums[s]
                s+=1
                e-=1
        else:
            nxtElem = pivot+1
            curSucc = None
            while nxtElem < len(nums):
                if nums[nxtElem]>nums[pivot]:
                    if curSucc == None or nums[curSucc]>=nums[nxtElem]:
                        curSucc = nxtElem
                nxtElem += 1
            print(pivot, curSucc)
            if(curSucc and pivot<len(nums) and curSucc<len(nums)):
                nums[pivot], nums[curSucc] = nums[curSucc], nums[pivot]
            
            s = pivot+1
            e = len(nums)-1
            
            while s<e:
                nums[s], nums[e] = nums[e], nums[s]
                s+=1
                e-=1
        