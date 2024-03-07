from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = maxProduct = minProduct = nums[0]
        
        for i in range(1, len(nums)):
            maxProdMult = maxProduct * nums[i]
            minProdMult = minProduct * nums[i]
            maxProduct = max(minProdMult,maxProdMult, nums[i])
            minProduct = min(minProdMult,maxProdMult, nums[i])    
            result = max(maxProduct, result)
        
        return result