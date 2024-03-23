from logging import critical
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adjList = {}
        for i in range(n):
            adjList[i] = []
        for u,v in connections:
            adjList[u].append(v)
            adjList[v].append(u)
        
        
        visited = set()
        DISCOVERY_TIME = 0
        nodeLow = {}
        nodeDisc = {}
        critical = []
        
        
        def dfs(u, parent):
            nonlocal DISCOVERY_TIME
            visited.add(u)
            nodeLow[u] = nodeDisc[u] = DISCOVERY_TIME
            DISCOVERY_TIME+=1
            
            for v in adjList[u]:
                if v == parent:
                    continue
                elif v not in visited:
                    dfs(v, u)
                    nodeLow[u] = min(nodeLow[u], nodeLow[v])
                    
                    if nodeLow[v] > nodeDisc[u]:
                        critical.append([u,v])
                else:
                    nodeLow[u] = min(nodeLow[u], nodeDisc[v])

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
        
        return critical

s = Solution()

print(s.criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]]))
        
print(s.criticalConnections(6,[[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]))