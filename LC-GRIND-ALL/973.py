from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for p in points:
            dist = p[0]**2  + p[1]**2
            heap.append((dist, p))
        
        heapq.heapify(heap)
        res = []
        while k:
            dist, p = heapq.heappop(heap)
            res.append(p)
            k-=1
        return res