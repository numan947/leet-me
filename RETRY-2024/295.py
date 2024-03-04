import heapq
class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    ## Considering the stream as 1, 2, 3, 4, 5, 6, 7...
    ## MaxHeap contains the lower half, and minHeap contains the upper half
    ## We start by adding to the upper half
    ## if both heaps are equal in size => add to the minHeap, always the size difference must be maintained at 1


    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            if not self.minHeap:
                heapq.heappush(self.minHeap, num)
                return
            
            ## we need to make sure minHeap has more elements
            tMaxHeap = - self.maxHeap[0]
            if num>=tMaxHeap: # top of maxheap will always be less or equal to top of minHeap top
                # just add to the minHeap
                heapq.heappush(self.minHeap, num)
            else:
                val = heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap, -num)
                heapq.heappush(self.minHeap, -val)
        else:
            ## length is not equal, so we can possibly make them equal
            tMinHeap = self.minHeap[0]
            
            if num<=tMinHeap:
                heapq.heappush(self.maxHeap, -num)
            else:
                val = heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, num)
                heapq.heappush(self.maxHeap, -val)    
                
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return ((-self.maxHeap[0]) + self.minHeap[0])/2.0
        else:
            return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()