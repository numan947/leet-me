class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        minsum = sum(nums)
        found = False

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    num_i = nums[i]
                    num_j = nums[j]
                    num_k = nums[k]
                    if num_i<num_j>num_k:
                        minsum = min(minsum, num_i+num_j+num_k)
                        found = True
        
        if found:
            return minsum
        return -1
