class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        totalArea = (ay2-ay1) * (ax2-ax1) + (by2-by1)*(bx2-bx1)
        left, right = max(ax1, bx1), min(ax2, bx2)
        xOverlap = right - left
        top, bottom = min(ay2, by2), max(ay1, by1)
        yOverlap = top-bottom
        
        if xOverlap>0 and yOverlap>0:
            totalArea -= (xOverlap*yOverlap)
        return totalArea