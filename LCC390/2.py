import math
class Solution:
    def minOperations(self, k: int) -> int:
        convertToMax = k
        if convertToMax == 0:
            return k - 1
        
        ans2 = float('inf')
        for convertTo in range(1, convertToMax+1):
            stepsNeeded = convertTo - 1
            # duplicate counts
            dupsNeeded = math.ceil(k/convertTo) - 1 # -1 for the initial value
            
            ans2 = min(ans2, dupsNeeded + stepsNeeded)
        
        return ans2

s = Solution()

# print(s.minOperations(9))
# print(s.minOperations(36))
# print(s.minOperations(7))
# print(s.minOperations(5))
# print(s.minOperations(11))
# print(s.minOperations(25))
# print(s.minOperations(49))
print(s.minOperations(100))