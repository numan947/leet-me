from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        res = []
        i = 0
        while i<len(nums):
            L = i+1
            R = len(nums)-1

            while L<R:
                curSum = (nums[i] + nums[L] + nums[R])
                if (curSum == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    L+=1
                    R-=1
                    while L<R and nums[L] == nums[L-1]:
                        L+=1
                    while L<R and nums[R] == nums[R+1]:
                        R-=1
                elif curSum < 0: # we cannot get a larger value moving right pointer
                    L += 1    
                    # # update L
                    while L<R and nums[L] == nums[L-1]:
                        L+=1
                elif curSum > 0: # We cannot get a smaller value moving left pointer
                    R = R - 1
                    while L<R and nums[R] == nums[R+1]:
                        R-=1
            # update i
            i+=1
            while i<len(nums) and nums[i] == nums[i-1]:
                i+=1
        
        return res

s = Solution()

print(s.threeSum(nums = [-1, 0,1,2,-1,-4]))
print(s.threeSum([-2,0,0,2,2]))
print(s.threeSum([1,-1,-1,0]))