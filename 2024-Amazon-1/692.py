from collections import defaultdict
from functools import cmp_to_key
import heapq
from typing import List

class Elem:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        else:
            return self.count<other.count
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
    
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for w in words:
            freq[w]+=1
        
        
        minHeap = []
        for key, val in freq.items():
            # if minHeap:
            #     print(minHeap[0].word, minHeap[0].count)
            heapq.heappush(minHeap, (Elem(val, key)))
            if len(minHeap)>k:
                e = heapq.heappop(minHeap)
                # print("popped --> ", e.word, e.count)
        
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap).word) # popping ensures that we don't need any extra sorting
        
        return res[::-1]

s = Solution()


print(s.topKFrequent(["aaa","aa", "a"], 2))
print(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))

print(s.topKFrequent(["i","love","leetcode","i","love","coding"], k=3))