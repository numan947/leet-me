class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def solve(remain):
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            
            cnt = 0
            for n in nums:
                cnt += solve(remain - n)
            
            return cnt
        
        return solve(target)