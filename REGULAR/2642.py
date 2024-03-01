from typing import List


class Graph:
    def relax(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dist[i][j] > (self.dist[i][k] + self.dist[k][j]):
                        self.dist[i][j] = (self.dist[i][k] + self.dist[k][j])

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        for t in range(self.n):
            self.dist[t][t] = 0
                
        for e in edges:
            u,v,w = e
            self.dist[u][v] = w
        self.relax()
        
    def addEdge(self, edge: List[int]) -> None:
        u, v, w = edge
        # self.dist[u][v] = w
        for i in range(self.n):
            for j in range(self.n):
                if self.dist[i][j] > (self.dist[i][u] + self.dist[v][j] + w):
                    self.dist[i][j] = (self.dist[i][u] + self.dist[v][j] + w)
        
    def shortestPath(self, node1: int, node2: int) -> int:
        dist = self.dist[node1][node2]
        if dist == float('inf'):
            return -1
        return dist


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])

# 'nei':[],
# 			'wgt':[]