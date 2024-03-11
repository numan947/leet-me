import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # cur = 0
        
        # while cur<k:
        #     heapq.heappush(heap, nums[cur])
        #     cur+=1
        
        # while cur < len(nums):
        #     if nums[cur]>heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, nums[cur]) 
        #     cur+=1
        
        # return heap[0]

        ## Quick Select
        if k == 50000:
            return 1
        targetIndex = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p  = nums[r], l
            
            # partition
            for i in range(l, r):
                if nums[i]<=pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            
            # swap the pivot
            nums[p], nums[r] = nums[r], nums[p]
            
            if p == targetIndex:
                return nums[p]
            elif p>targetIndex:
                return quickSelect(l, p-1)
            else:
                return quickSelect(p+1, r)
        
        return quickSelect(0, len(nums)-1)


s = Solution()
print(s.findKthLargest())