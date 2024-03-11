from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        visited = set()
        adjList = {}
        for u,v in edges:
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []
            adjList[u].append(v)
            adjList[v].append(u)
        for i in range(n):
            if i not in adjList:
                adjList[i] = []
        
        def dfs(nd, pr): # current node, parent
            if nd in visited:
                return False
            visited.add(nd)
            
            OK = True
            for nei in adjList[nd]:
                if nei != pr:
                    OK = OK and dfs(nei, nd)
                if not OK:
                    return False
            return OK
        
        
        return dfs(0, -1) and len(visited) == n


s = Solution()

# print(s.valid_tree(n = 5 , edges = [[0, 1], [0, 2], [0, 3], [1, 4]]))
# print(s.valid_tree(n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
# print(s.valid_tree(1, []))