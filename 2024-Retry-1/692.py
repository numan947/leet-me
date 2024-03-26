import heapq
from typing import List


class ELEM:
    def __init__(self, w, f):
        self.wrd = w
        self.frq = f

    def __lt__(self, other):
        if self.frq == other.frq:
            return self.wrd > other.wrd # because we want to pop lexicographically large elements first in case of draw 
        else:
            return self.frq<other.frq # we want to remove smaller count elements first
        
    def __eq__(self, other):
        return self.frq == other.frq and self.wrd == other.wrd
    
            

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frq = {}
        for w in words:
            frq[w] = frq.get(w, 0) + 1
        
        heap = [] # maxHeap
        for w,v in frq.items():
            e = ELEM(w, v)
            heapq.heappush(heap, e)
            if len(heap)>k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap).wrd)
        return res[::-1]