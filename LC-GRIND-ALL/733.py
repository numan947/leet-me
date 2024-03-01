from typing import List

from apt import Cache


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        @cache
        def flood(curR, curC, srcColor, tgtColor):
            if curR>=len(image) or curR<0 or curC>=len(image[0]) or curC<0 or image[curR][curC]!=srcColor or image[curR][curC] == tgtColor:
                return
            image[curR][curC] = tgtColor
            
            flood(curR+1, curC, srcColor, tgtColor)
            flood(curR-1, curC, srcColor, tgtColor)
            flood(curR, curC+1, srcColor, tgtColor)
            flood(curR, curC-1, srcColor, tgtColor)
            return
        
        flood(sr, sc, image[sr][sc], color)
        
        return image