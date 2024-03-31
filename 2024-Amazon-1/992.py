from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
		## SOLUTION WITH SLIDING WINDOW WITH THREE POINTERS
        # count = defaultdict(int)
        # res = 0
        # l_far = l_near = 0
        
        # for r in range(len(nums)):
        #     count[nums[r]] += 1
            
        #     while len(count)>k:
        #         count[nums[l_near]] -= 1
        #         if count[nums[l_near]] == 0:
        #             count.pop(nums[l_near])
        #         l_near+=1
        #         l_far = l_near
        #     while count[nums[l_near]]>1:
        #         count[nums[l_near]]-=1
        #         l_near+=1
            
        #     if len(count) == k:
        #         res += (l_near - l_far + 1)
        # return res
        
        ## SOLUTION WITH SLIDING WINDOW WITH TWO POINTERS => AT_MOST_K - AT_MOST_K-1
        
        def findAtMostK(kk):
            l = 0
            res = 0
            seen = defaultdict(int)
            for r in range(len(nums)):
                seen[nums[r]] += 1
                while l<r and len(seen)>kk:
                    seen[nums[l]]-=1
                    if seen[nums[l]] == 0:
                        seen.pop(nums[l])
                    l+=1
                if len(seen) <= kk:
                    res += (r-l+1)
            return res
        # print(findAtMostK(k), findAtMostK(k-1))
        return findAtMostK(k) - findAtMostK(k-1)

s = Solution()
print(s.subarraysWithKDistinct([1,2,1,2,3], 2))