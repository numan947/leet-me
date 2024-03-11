from collections import deque
from operator import ne
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        inDegree = {}
        
        for n in range(numCourses):
            adjList[n] = []
            inDegree[n] = 0
        for v,u in prerequisites: # u --> v
            adjList[u].append(v)
            inDegree[v]+=1
        dq = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                dq.append(i)
        order = []
        
        
        while dq:
            cur = dq.popleft()
            order.append(cur)
            
            for nei in adjList[cur]:
                inDegree[nei]-=1
                if inDegree[nei] == 0:
                    dq.append(nei)
        
        # order.reverse()
        if len(order) == numCourses:
            return order
        return []
            
        