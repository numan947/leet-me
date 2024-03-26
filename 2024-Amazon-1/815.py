from collections import defaultdict, deque
from typing import List


"""

1. BFS elements are the stations
2. To get to the next station, we can take all the buses available in that station and go to the next station
3. To do that we need to map which buses can be taken from each station.
4. During BFS, we update the queue, using the destination after taking the buses available at that station.
5. To make sure we terminate and find the lowest distance -- 
6. we must not take the same bus twice -- keep a hashset
7. we must not visit the same station twice -- keep a hashset
8. Reasoning is=> if we can get to the target minimally from a node, we will do that in the first try in bfs

"""


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stationMap = defaultdict(set) # (stationId, [bus1, bus2, bus3....])
        
        for busId, route in enumerate(routes):
            for station in route:
                if station not in stationMap:
                    stationMap[station] = set()
                stationMap[station].add(busId)
        
        dq = deque([(source, 0)])
        stationSeen = set([source])
        busSeen = set()
        
        while dq:
            curStation, dist = dq.popleft()
            
            if curStation == target:
                return dist
            
            for bus in stationMap[curStation]:
                if bus in busSeen:
                    continue # 1. don't take the same bus
                busSeen.add(bus)
                for station in routes[bus]:
                    if station in stationSeen:
                        continue # don't take the same station
                    stationSeen.add(station)
                    dq.append((station, 1+dist))
        
        return -1
        

s = Solution()

print(s.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
print(s.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12))