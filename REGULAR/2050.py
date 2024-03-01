from typing import List
from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        nodes = [{'id':i, 'out':0, 'in':0} for i in range(n)]
        adjList = {i:[] for i in range(n)} 
        
        for f,t in relations:
            f-=1
            t-=1
            nodes[f]['out'] += 1
            nodes[t]['in'] += 1
            adjList[f].append(t)
        # print(nodes)
        
        dq = deque()
        
        for n in nodes:
            if n['in'] == 0:
                dq.append(n)
        
        ans = 0
        while dq:
            tmpAns = 0
            sz = len(dq)
            for t in range(sz):
                curNode = dq.popleft()
                id = curNode['id']
                tmpAns = max(tmpAns, time[id])
                
                for nei in adjList[id]:
                    nodes[nei]['in'] -= 1
                    if nodes[nei]['in'] == 0:
                        dq.append(nodes[nei])
            print(tmpAns)
            ans += tmpAns
        
        return ans


s = Solution()

# print(s.minimumTime(3,[[1,3],[2,3]],[3,2,5]))
print(s.minimumTime(9,[[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]],[9,5,9,5,8,7,7,8,4]))