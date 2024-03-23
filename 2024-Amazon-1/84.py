from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        
        stack = [] # contains (height, position)
        
        for i, h in enumerate(heights):
            tmpI = i
            while stack and stack[-1][0]>h:
                curH, curP = stack.pop()
                width = i - curP
                height = curH
                maxArea = max(maxArea, height*width)
                tmpI = curP
            stack.append((h, tmpI))

        pos = len(heights)
        while stack:
            curH, curP = stack.pop()
            maxArea = max(maxArea, curH*(pos-curP))
        return maxArea
    
s = Solution()

print(s.largestRectangleArea([2,1,2]))
print(s.largestRectangleArea(heights = [2,1,5,6,2,3]))
print(s.largestRectangleArea(heights = [2,4]))