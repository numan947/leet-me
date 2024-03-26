from collections import defaultdict
import heapq
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        freqMap = {} # (val -> count)
        maxHeap = [] # (count, val)
        res = [] 
        
        for i in range(len(nums)):
            freqMap[nums[i]] = freqMap.get(nums[i], 0) + freq[i]
            # update the heap
            if maxHeap and maxHeap[0][1] == nums[i]: # current number is in the top of the heap
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-freqMap[nums[i]], nums[i])) # adjust
            else:
                heapq.heappush(maxHeap, (-freqMap[nums[i]], nums[i]))
            while freqMap[maxHeap[0][1]]!= -maxHeap[0][0]: # update the outdated top number
                _, n = heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, (-freqMap[n], n))
            res.append(-maxHeap[0][0])
        
        return res

s = Solution()
# print(s.mostFrequentIDs(nums = [2,3,2,1], freq = [3,2,-3,1]))
# print(s.mostFrequentIDs(nums = [5,5,3], freq = [2,-2,1]))
print(s.mostFrequentIDs([5,3,9,4,3,9,4] , [2,4,5,2,-2,-4,5]))