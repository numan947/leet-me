from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        seenSofar = defaultdict(int)
        seenSofar[0]=1
        count = 0
        tmpSum = 0
        for i in range(len(nums)):
            tmpSum += nums[i]
            if (tmpSum-k) in seenSofar:
                count+= seenSofar[(tmpSum-k)]
            seenSofar[tmpSum]+=1
        return count


s = Solution()
print(s.subarraySum([1,-1,0], 0))
# print(s.subarraySum([1,2,3], 3))