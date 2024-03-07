from collections import deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskLists = {}
        for t in tasks:
            if t not in taskLists:
                taskLists[t] = 0
            taskLists[t] += 1
        
        waitQueue = deque()
        maxHeap = []
        curTime = 0
        
        for k,v in taskLists.items():
            heapq.heappush(maxHeap, (-v, 0, k)) # (tasksLeft, readyTime, id)
        
        
        while maxHeap or waitQueue:
            # print(curTime)
            if maxHeap:
                tasksLeft, readyTime, id = heapq.heappop(maxHeap)
                tasksLeft += 1
                readyTime = curTime + n
                if tasksLeft !=0:
                    waitQueue.append((tasksLeft, readyTime, id))
            while waitQueue and waitQueue[0][1]<=curTime:
                heapq.heappush(maxHeap, waitQueue.popleft())
            curTime += 1
            
        return curTime
                    
        
    


s = Solution()


print(s.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(s.leastInterval(tasks = ["A","C","A","B","D","B"], n = 1))
print(s.leastInterval(tasks = ["A","A","A", "B","B","B"], n = 3))
print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 1))