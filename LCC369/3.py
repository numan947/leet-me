from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        def findMax(i):
            
            mx = max(nums[i], nums[i-1])
            if mx == nums[i]:
                return (mx, i)
            elif mx == nums[i-1]:
                return (mx, i-1)
        
        def isBeautiful(i, k):
            return nums[i]>=k or nums[i-1]>=k or nums[i-2]>=k
        
        n = len(nums)
        ops = 0
        
        dp = {}
        def solve(curPos):
            if curPos in dp:
                return dp[curPos]
            if curPos>=n:
                return 0
            
            cost = float('inf')
            if isBeautiful(curPos, k):
                cost = solve(curPos+1)
            
            tmp = nums[curPos]
            nums[curPos] = k
            cost = min(cost, (k-tmp)+(solve(curPos+1)))
            nums[curPos] = tmp
            return cost
        print(nums)
        return solve(2)

s = Solution()
print(s.minIncrementOperations([43,31,14,4], 73))
print(s.minIncrementOperations([2,3,0,0,2], 4))

print(s.minIncrementOperations([13,34,0,13,9,19], 82)) #117