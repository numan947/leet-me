from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Find the pivot -> the element from the end of the list where it's not in  monotonically descending order (i.e. increasing order from the end)
        pivot = len(nums)-2 # as we need to compare with the last element
        while pivot>=0 and nums[pivot]>=nums[pivot+1]:
            pivot-=1
        
        ## CASE: if we cannot find such element, the entire array is sorted in reversed
        if pivot < 0:
            nums.reverse()
            return
        
        # Else we can create another permutation: find the smallest element greater than the pivot on the right side of the pivot
        ans = pivot+1
        val = nums[pivot+1]
        tmp = pivot+1
        
        while tmp<len(nums):
            if nums[tmp]>nums[pivot]:
                val = nums[tmp]
                ans = tmp
            tmp+=1
        
        nums[pivot], nums[ans] = nums[ans], nums[pivot]
        
        print(pivot)
        ## Reverse the array from pivot to end
        l = pivot+1
        r = len(nums)-1
        
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1


s = Solution()
print(s.nextPermutation([1,5,1]))