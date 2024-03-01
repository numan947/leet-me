from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjCnt = {}
        adj = {}
        
        for l in adjacentPairs:
            a, b = l
            adjCnt[a] = adjCnt.get(a, 0) + 1
            adjCnt[b] = adjCnt.get(b, 0) + 1
            if a not in adj:
                adj[a] = []
            adj[a].append(b)
            if b not in adj:
                adj[b] = []
            adj[b].append(a)
        start = None
        for t in adjCnt.keys():
            if adjCnt[t] == 1:
                start = t
                break
        res2 = []
        res = set()
        while len(res) < len(adjacentPairs)+1:
            res.add(start)
            res2.append(start)
            adjArr = adj[start]
            
            for t in adjArr:
                if t in res:
                    continue
                start = t
                break
        return list(res2)   
s = Solution()

s.restoreArray( [[4,-2],[1,4],[-3,1]])