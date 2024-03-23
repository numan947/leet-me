from collections import defaultdict, deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        waitQ = deque()
        freqMap = defaultdict(int)
        
        for t in tasks:
            freqMap[t] += 1
        maxHeap = [(-v, k) for (k,v) in freqMap.items()]
        heapq.heapify(maxHeap)
        
        curTime = 0
        
        
        while maxHeap or waitQ:
            if maxHeap:
                curLeft, curKey = heapq.heappop(maxHeap)
                curLeft+=1
                
                if curLeft!=0:
                    waitQ.append(((curLeft, curKey), curTime+n))
                    
            while waitQ and waitQ[0][1]<=curTime:
                heapq.heappush(maxHeap, waitQ.popleft()[0])
            curTime+=1
        
        return curTime