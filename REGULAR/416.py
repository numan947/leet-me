from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # this is basically 0-1 knapsack
        dp = {}
        
        def dfs(idx, targetSum):
            if (idx,targetSum) in dp:
                return dp[(idx,targetSum)]
            if targetSum == 0:
                return True
            if targetSum<0:
                return False
            if idx == len(nums):
                return False
            
            if (dfs(idx+1, targetSum)):
                dp[(idx,targetSum)] = True
                return True
            if (dfs(idx+1, targetSum - nums[idx])):
                dp[(idx,targetSum)] = True
                return True
            dp[(idx,targetSum)] = False
            return False
        
        s = sum(nums)
        
        if s%2:
            return False
        else:
            return dfs(0, s//2)


s = Solution()
print(s.canPartition([1,5,11,5]))