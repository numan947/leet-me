from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curSum = 0
        seenBefore = {0:0} # so that we can get the full length of the binary array
        mxLength = 0
        for i, n in enumerate(nums):
            if n:
                curSum+=1
            else:
                curSum-=1            
            if curSum in seenBefore:
                mxLength = max(mxLength, i+1-seenBefore[curSum])
            else:
                seenBefore[curSum] = i+1
                
        return mxLength

s = Solution()

print(s.findMaxLength([0,1]))
print(s.findMaxLength([0,1,0]))
print(s.findMaxLength([0,1,0,1]))