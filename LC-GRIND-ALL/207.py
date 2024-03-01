from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0 or len(prerequisites) == 0:
            return True
        incoming = {}
        adjList = {}
        for a, b in prerequisites:
            if a not in adjList:
                adjList[a] = []
            if b not in adjList:
                adjList[b] = []
            adjList[a].append(b)
            incoming[b] = incoming.get(b, 0) + 1
        
        dq = deque()
        
        for i in range(numCourses):
            if i not in incoming:
                incoming[i] = 0
            if i not in adjList:
                adjList[i] = []
            cin = incoming.get(i, 0)
            if cin == 0:
                dq.append(i)
                
        order = []
        while dq:
            t = dq.popleft()
            order.append(t)
            for nb in adjList[t]:
                incoming[nb] -= 1
                if incoming[nb] == 0:
                    dq.append(nb)
            
        return len(order) == numCourses
        
        

s = Solution()

print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(1, []))