from typing import List


class Solution:
    def asteroidCollision(self, all_ast: List[int]) -> List[int]:
        asteriods = []
        
        for ast in all_ast:
            add = ast
            while asteriods and ((asteriods[-1]>0 and ast<0)):
                if abs(asteriods[-1]) < abs(ast):
                    asteriods.pop()
                elif abs(asteriods[-1]) == abs(ast):
                    asteriods.pop()
                    add = None
                    break
                else:
                    add = None
                    break
            if add:
                asteriods.append(add)
            
        return asteriods


s = Solution()

print(s.asteroidCollision([5,10,-5]))
print(s.asteroidCollision([-2,-1,1,2]))