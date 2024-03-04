from typing import List
import heapq

class MedianFinder:
    def __init__(self, k:int):
        self.k = k
        self.maxHeap = [] # max heap stores the smaller half
        self.minHeap = [] # min heap stores the larger half, assume this can be 1 greater in size than maxHeap
        self.deleted = {} # delayed deleted items, should be a counter
        self.minHeapSize = 0
        self.maxHeapSize = 0
    
    def add(self, num:int):
        if not self.minHeap or num>=self.minHeap[0]: # this should be part of the minheap
            heapq.heappush(self.minHeap, num)
            self.minHeapSize += 1
        else:
            heapq.heappush(self.maxHeap, -num)
            self.maxHeapSize += 1
        self.rebalance()
    
    def rebalance(self):
        while self.minHeapSize > self.maxHeapSize + 1: # minHeapSize can be at most 1 greater than maxHeapSize, this condition indicates, minheap has expired items
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            self.minHeapSize -= 1
            self.maxHeapSize += 1
            self.prune(self.minHeap)

        while self.minHeapSize<self.maxHeapSize: # minHeapSize must be 1 greater than maxHeapSize or equal, so the extra item has to be in maxHeap
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            self.maxHeapSize -=1
            self.minHeapSize +=1
            self.prune(self.maxHeap)
    
    def prune(self, heap):
        mul  = 1
        if heap == self.maxHeap:
            mul = -1
        ## fix the lookup
        
        while heap and self.deleted.get(mul*heap[0], 0)>0:
            self.deleted[mul*heap[0]] -= 1
            heapq.heappop(heap)    
    
    def remove(self, num:int):
        self.deleted[num] = self.deleted.get(num, 0) + 1
        
        if num >= self.minHeap[0]: # num is actually part of the minHeap
            self.minHeapSize -= 1
            if num == self.minHeap[0]:
                self.prune(self.minHeap)
        else:
            self.maxHeapSize -= 1
            if num == -self.maxHeap[0]:
                self.prune(self.maxHeap)
        self.rebalance()
    
    def find_median(self):
        # print(self.minHeap)
        # print(self.maxHeap)
        # print("------------------")
        if self.k%2 == 1:
            return self.minHeap[0]
        else:
            return (-self.maxHeap[0]+self.minHeap[0])/2.0


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        finder = MedianFinder(k)
        
        for x in nums[:k]:
            finder.add(x)
        ans = [finder.find_median()]
        for i in range(k, len(nums)):
            finder.add(nums[i])
            finder.remove(nums[i-k])
            ans.append(finder.find_median())
        return ans
        


s = Solution()

print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], k=3))

print(s.medianSlidingWindow( [1,2,3,4,2,3,1,4,2], 3))

print(s.medianSlidingWindow([7,9,3,8,0,2,4,8,3,9], 1))