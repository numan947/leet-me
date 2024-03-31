import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap = [] # contain (value, pos)
        maxHeap = [] # contain (value, pos)
        l = r = 0
        longest = 1
        while r<len(nums):
            heapq.heappush(minHeap, (nums[r], r))
            heapq.heappush(maxHeap, (-nums[r], r))
            while l<r and abs(minHeap[0][0] + maxHeap[0][0]) > limit:
                l+=1
                while minHeap[0][1]<l:
                    heapq.heappop(minHeap)
                while maxHeap[0][1]<l:
                    heapq.heappop(maxHeap)
            if minHeap and maxHeap:
                longest = max(longest, r-l+1)
            r+=1
        return longest

s = Solution()

print(s.longestSubarray(nums = [8,2,4,7], limit = 4))
print(s.longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0))
print(s.longestSubarray(nums = [10,1,2,4,7,2], limit = 5))