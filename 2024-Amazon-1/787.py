from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ## basically bellman ford algorithm
        dist = [float('inf')]*n
        dist[src] = 0
        
        for _ in range(k+1):
            tmpDist = [x for x in dist] # make a copy to edit
            
            # go over each edge and relax
            for u,v,w in flights:
                if dist[u]!=float('inf'): #dist[u] is reachable
                    if tmpDist[v] > dist[u] + w: # remember we are updating tmpDist[v] so we need to compare accordingly
                        tmpDist[v] = dist[u] + w
            
            dist = [x for x in tmpDist]
        
        return -1 if dist[dst] == float('inf') else dist[dst]


s = Solution()

print(s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
print(s.findCheapestPrice(7, [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],[1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]], 2, 4, 1))