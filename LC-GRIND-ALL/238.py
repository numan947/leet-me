from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = []
        for n in nums:
            res.append(prefix)
            prefix*=n
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * suffix
            suffix *=nums[i]
        return res


s = Solution()

print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))