from typing import List
from collections import deque

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque()
        max_elem = max(arr) # this is the insight!!
        
        winstreak = 0
        lastWinner = -1
        for t in arr:
            q.append(t)
        while q:
            first = q.popleft()
            second = q.popleft()
            if winstreak == k:
                return first
            
            winner = max(first, second)
            loser = min(first, second)
            if winner == max_elem:
                return winner
            # print(winner, loser)
            if winner == lastWinner:
                winstreak += 1
            else:
                lastWinner = winner
                winstreak = 1
            q.appendleft(winner)
            q.append(loser)
        
        return -1
    


s = Solution()

print(s.getWinner(arr = [2,1,3,5,4,6,7], k = 2))