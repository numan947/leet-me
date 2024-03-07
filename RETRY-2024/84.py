from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(index, height)
        result = 0
        for i in range(len(heights)):
            earliest_possble = i
            while stack and stack[-1][1]>heights[i]:
                idx, ht = stack.pop()
                width = (i - idx)
                # print(width*ht)
                result = max(result, width * ht)
                earliest_possble = min(earliest_possble, idx)
            stack.append((earliest_possble, heights[i]))
        while stack:
            idx, ht = stack.pop()
            width = len(heights) - idx
            result = max(result, width * ht)
        return result


s = Solution()

print(s.largestRectangleArea([2,1,5,6,2,3]))
print(s.largestRectangleArea([2,1,2]))