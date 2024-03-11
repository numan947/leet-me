from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mx = 0
        balance = 0
        lastSeen = {0:0}## 0 is reserved, each char is 1 index to make sure we consider the whole array as a possibility
        
        for i in range(len(nums)):
            addi = 1 if nums[i] else -1
            balance+=addi
            
            if balance in lastSeen:
                #we have seen this count before, so there has to be equal number of
                # 1s and zeros between current and the last post
                lastPos = lastSeen[balance]
                mx = max(mx, (i+1)-lastPos)
            else:
                lastSeen[balance] = (i+1)
        return mx


s = Solution()
print(s.findMaxLength([0,1,0,1]))