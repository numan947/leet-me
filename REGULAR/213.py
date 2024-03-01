class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:  # only edge case
            return sum(nums)

        @cache
        def solve(idx, z):
            if idx >= len(nums):
                return 0

            gain = 0
            if idx == len(nums)-1:
                if not z:
                    gain  = max(gain, nums[idx]+solve(idx+2, z))    
            else:
                gain  = max(gain, nums[idx]+solve(idx+2, z))
            
            gain = max(gain, solve(idx+1,z))
            
            return gain
        
        return max(solve(0, True), solve(1, False))