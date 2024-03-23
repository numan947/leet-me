from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def countTarget(curDice, remain):
            if remain == 0 and curDice == n:
                return 1
            if curDice == n or remain<0:
                return 0
            
            cnt = 0
            
            for v in range(1, k+1):
                cnt += countTarget(curDice+1, remain-v)
                cnt%=int(1e9+7)
            
            return cnt%int(1e9+7)
        
        return countTarget(0, target)

s = Solution()

print(s.numRollsToTarget(30, 30, 500))