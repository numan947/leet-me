from collections import deque
from typing import List


        
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square-1)//length
            c = (square-1)%length
            if r%2:
                c = length-1-c
            return [r, c]
        
        
        q = deque([[1, 0]]) # (curPos, dist)
        visit = set()
        
        while q:
            cur, dist = q.popleft()            
            for i in range(1, 7):
                nextSquare = cur + i
                r,c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return dist + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, dist+1])
        # flat = [0]
        # for b in range(len(board)-1, -1, -1):
        #     if b%2==0:
        #         for i in range(len(board[b])-1, -1, -1):
        #             flat.append(board[b][i])
        #     else:
        #         for i in range(len(board[b])):
        #             flat.append(board[b][i])
        
        # dq = deque([1])
        # dist = {1:0}
        
        # while dq:
        #     cur = dq.popleft()
        #     if cur == len(flat)-1:
        #         return dist[cur]
        #     for t in range(1, 7): # 1...6
        #         nxt = cur+t
        #         if nxt>=len(flat):
        #             continue
        #         if flat[nxt]!=-1:
        #             nxt = flat[nxt]
        #         if nxt not in dist: 
        #             dist[nxt] = dist[cur] + 1
        #             dq.append(nxt)
        return -1
    
    
s = Solution()

print(s.snakesAndLadders(
    [
        [-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))

print(s.snakesAndLadders(board = [[-1,-1],[-1,3]]))

print(s.snakesAndLadders([[-1,-1,27,13,-1,25,-1],
[-1,-1,-1,-1,-1,-1,-1],
[44,-1,8,-1,-1,2,-1],
[-1,30,-1,-1,-1,-1,-1],
[3,-1,20,-1,46,6,-1],
[-1,-1,-1,-1,-1,-1,29],
[-1,29,21,33,-1,-1,-1]]))

print(s.snakesAndLadders([[-1,-1],[-1,1]]))
print(s.snakesAndLadders([[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]))
print(s.snakesAndLadders([[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]))