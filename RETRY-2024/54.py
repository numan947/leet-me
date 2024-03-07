from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        LEFT, RIGHT = 0, len(matrix[0])-1
        TOP, BOTTOM = 0, len(matrix)-1
        
        result = []
        
        while LEFT <= RIGHT and TOP <= BOTTOM:
            p = LEFT
            # Go from left to right
            while p <= RIGHT:
                result.append(matrix[TOP][p])
                p+=1
            TOP+=1
            
            p = TOP
            while p <= BOTTOM:
                result.append(matrix[p][RIGHT])
                p+=1
                
            RIGHT-=1
            
            if not (LEFT <= RIGHT and TOP <= BOTTOM):
                break
            
            
            p = RIGHT
            
            while p>=LEFT:
                result.append(matrix[BOTTOM][p])
                p-=1
            
            BOTTOM-=1
            
            p = BOTTOM
            
            while p>=TOP:
                result.append(matrix[p][LEFT])
                p-=1
                
            LEFT+=1
            
        return result
    



s = Solution()

print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))