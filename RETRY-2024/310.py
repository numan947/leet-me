from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        degree = {}
        adjList = {}
        
        for u,v in edges:
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []
            
            adjList[u].append(v)
            adjList[v].append(u)
            degree[u] = degree.get(u, 0) + 1
            degree[v] = degree.get(v, 0) + 1
        dq = deque()
        for i in range(n):
            if degree[i] == 1:
                dq.append(i)        
        totalLeft = n
        while totalLeft>2:
            #level order traversal
            levelSize = len(dq)
            for i in range(levelSize):
                u = dq.popleft()
                degree[u]-=1
                totalLeft -=1
                for v in adjList[u]:
                    degree[v]-=1
                    if degree[v] == 1:
                        dq.append(v)
        return list(dq)


s = Solution()

print(s.findMinHeightTrees(n = 4, edges = [[1,0],[1,2],[1,3]]))
print(s.findMinHeightTrees( n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(s.findMinHeightTrees(6,[[0,1],[0,2],[0,3],[3,4],[4,5]]))