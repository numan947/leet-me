from collections import deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
                
        routesSet = [set(r) for r in routes ]
        
        busesForStop = {}
        busesForStop[source] = []
        busesForStop[target] = []
        for bus, stops in enumerate(routes):
            for stop in stops:
                if stop not in busesForStop.keys():
                    busesForStop[stop] = []
                busesForStop[stop].append(bus)
        
        queue = deque([source])
        visited = set()
        
        res = 0
        
        while queue:
            res += 1
            
            levelSize = len(queue)
            for _ in range(levelSize):
                curStop = queue.popleft()
                
                for bus in busesForStop[curStop]:
                    if bus not in visited:
                        visited.add(bus)
                        for stop in routesSet[bus]:
                            if stop == target:
                                return res
                            queue.append(stop)
        return -1
                