class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rect_a = rec1
        rect_b = rec2
        
        overlap = rect_a[1] < rect_b[3] and \
            rect_a[3] > rect_b[1] and \
            rect_a[2] > rect_b[0] and \
            rect_a[0] < rect_b[2]
        
        return overlap