from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res = 0
        
        while l<r:
            curArea = (r-l) * min(height[l], height[r])
            res = max(curArea, res)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return res
    