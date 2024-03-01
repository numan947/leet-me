from typing import List
import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        dq = collections.deque()
        dist = {}
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dist[(i,j)] = 0
                    dq.append((i,j))
        
        
        
        while dq:
            # print(dq)
            r,c = dq.popleft()
            
            for dr, dc in [[1,0], [0,1], [-1, 0], [0, -1]]:
                tr,tc = r+dr, c+dc
                
                if tr<0 or tr>=len(mat) or tc<0 or tc>=len(mat[0]):
                    continue
                
                if (tr,tc) not in dist.keys() or dist[(tr,tc)]>dist[(r,c)]+1:
                    dist[(tr,tc)] = dist[(r,c)]+1
                    dq.append((tr,tc))
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = dist[(i,j)]

        return mat