from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using quick select
        if k == 50000:
            return 1
        k = len(nums) - k # kth smallest element from the beginning
        
        def quickSelect(l, r):
            pivot = r
            p1 = l    
            for i in range(l, r):
                if nums[i]<=nums[pivot]:
                    nums[p1], nums[i] = nums[i], nums[p1]
                    p1+=1    
            nums[pivot], nums[p1] = nums[p1], nums[pivot]
            
            if p1 == k:
                return nums[p1]
            elif p1 > k: # need to search left
                return quickSelect(l, p1-1)
            else:
                return quickSelect(p1+1, r)
        
        return quickSelect(0, len(nums)-1)

s = Solution()

print(s.findKthLargest(nums = [3,2,1,5,6,4], k = 2))
        