from collections import deque
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maxHeap = []
        # res = []
        
        # for i in range(k):
        #     maxHeap.append((-nums[i], i)) # number, index
        
        # heapq.heapify(maxHeap)
        # res.append(-maxHeap[0][0])
        
        
        # for i in range(k, len(nums)):
        #     heapq.heappush(maxHeap, (-nums[i], i))
        #     while maxHeap and maxHeap[0][1]<=(i-k):
        #         heapq.heappop(maxHeap)
        #     res.append(-maxHeap[0][0])
        
        # return res
        
        ## MONOTONIC QUEUE ##
        
        dq = deque()
        res = []
        
        for i in range(len(nums)):
            if i>=k:
                res.append(dq[0][0])
            while dq and dq[-1][0]<nums[i]:
                dq.pop()
            dq.append((nums[i], i))
            while dq and dq[0][1]<=(i-k):
                dq.popleft()
        res.append(dq[0][0])
        return res
        
s = Solution()

print(s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(s.maxSlidingWindow(nums = [1], k = 1))