import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result = []
        wordCount:dict = {}
        for w in words:
            if w not in wordCount:
                wordCount[w] = 0
            wordCount[w]+=1
        
        wordCount = [(-val,key) for (key,val) in wordCount.items()]
        
        heapq.heapify(wordCount)
        
        while k:
            item = heapq.heappop(wordCount)
            result.append(item[1])
            k-=1
        return result





s = Solution()
print(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
print(s.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
print(s.topKFrequent(["i","love","leetcode","i","love","coding"], 3))