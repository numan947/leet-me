from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pivot = len(nums)-2
        
        while pivot>=0:
            if nums[pivot+1]<=nums[pivot]:
                pivot-=1
            else:
                break
        
        if pivot <0:
            nums.reverse()
            return
        
        else:
            p = pivot+1
            successor = -1
            while p<len(nums):
                if nums[p]>nums[pivot]:
                    successor = p
                p+=1
            # print(pivot, successor)

            nums[pivot], nums[successor] = nums[successor], nums[pivot]
            l = pivot+1
            r = len(nums)-1
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        
        # print(nums)
            
            
            


s = Solution()
s.nextPermutation([2,3,1])
s.nextPermutation([1,4,3,2])
s.nextPermutation( [1, 3, 5, 4, 2])
s.nextPermutation([1, 4, 2, 3, 5])