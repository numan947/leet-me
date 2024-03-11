from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 2 ways to solve: one is just use dfs + visit
        # another is using union find
        
        par = [i for i in range(n)]
        rank = [1]*n
        
        def find(nd):
            res = nd
            while res!=par[res]:
                par[res] = par[par[res]] # Path compression
                res = par[res]
            return res
        
        def union(nd1, nd2):
            p1, p2 = find(nd1), find(nd2)
            
            if p1 == p2:
                return 0
            
            if rank[p2]>rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
        
            return 1
        
        res = n
        for n1, n2 in edges:
            if union(n1, n2):
                res -=1
            
        return res
        
        
        
        
            
        
        
            