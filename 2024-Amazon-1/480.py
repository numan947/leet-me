import heapq
from typing import List


class MedianFinder:
    def __init__(self):
        self.minHeap = [] # contains the upper half, allowed to be 1 greater than maxHeap in size 
        self.maxHeap = [] # contains the lower half ELEMENTS=> (value, idx)
        self.minHeapSize = 0
        self.maxHeapSize = 0
        self.deleted = {}
    
    def add(self, value):
        # always add to minHeap
        if not self.minHeap or value >= self.minHeap[0]: # # mistake 1
            heapq.heappush(self.minHeap, value)
            self.minHeapSize+=1
        else:
            heapq.heappush(self.maxHeap, -value)
            self.maxHeapSize+=1
        self.rebalance()
    
    def rebalance(self):
        while self.minHeapSize>(1+self.maxHeapSize):
            value = heapq.heappop(self.minHeap)
            self.minHeapSize-=1
            heapq.heappush(self.maxHeap, -value)
            self.maxHeapSize+=1
            self.prune(self.minHeap)
            
        while self.maxHeapSize > self.minHeapSize:
            value= heapq.heappop(self.maxHeap)
            self.maxHeapSize-=1
            heapq.heappush(self.minHeap, -value)
            self.minHeapSize+=1
            self.prune(self.maxHeap, -1)
    
    def prune(self, heap, mult=1):
        while heap and self.deleted.get(mult*heap[0], 0)>0:
            self.deleted[mult*heap[0]] = self.deleted.get(mult*heap[0], 0) - 1
            heapq.heappop(heap) # # mistake 2
    
    def delete(self, num):
        self.deleted[num] = self.deleted.get(num, 0) + 1
        
        if num>=self.minHeap[0]:
            self.minHeapSize-=1
            if self.minHeap[0] == num:
                self.prune(self.minHeap)
        else:
            self.maxHeapSize-=1
            if self.maxHeap[0] == -num: # mistake 3
                self.prune(self.maxHeap, -1) # mistake 4
        self.rebalance()
    
    def find_median(self, k):
        if k%2:
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0])/2.0
            

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        finder = MedianFinder()
        
        for x in nums[:k]:
            finder.add(x)
        ans = [finder.find_median(k)]
        
        for i in range(k, len(nums)):
            finder.add(nums[i])
            finder.delete(nums[i-k])
            ans.append(finder.find_median(k))
        
        return ans
    

s = Solution()

print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(s.medianSlidingWindow([7,9,3,8,0,2,4,8,3,9], 1))