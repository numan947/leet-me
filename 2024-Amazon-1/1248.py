from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        s = l = r = 0
        count = 0
        oddCount = 0
        
        while r<len(nums):
            if nums[r]%2:
                if oddCount == 0:
                    l = r
                oddCount+=1
            
            if oddCount>k:
                s = l+1
                oddCount-=1 # just removed that one
                # find the next odd
                l+=1
                while nums[l]%2 == 0:
                    l+=1
            # print(s,l,r)
            # if oddCount == k:
                # print(s, l, r)
            count += (l - s + 1)
            r+=1
        return count


s = Solution()

# print(s.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
# print(s.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))
print(s.numberOfSubarrays([91473,45388,24720,35841,29648,77363,86290,58032,53752,87188,34428,85343,19801,73201], 4))
"""                          0     1      2     3    4     5     6     7     8     9     10    11    12    13"""