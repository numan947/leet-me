from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        maxPossibleScore = 0
        curScore = 0
        
        l, r = 0, len(tokens)-1
        
        while l<=r:            
            if power < tokens[l]:
                if curScore == 0:
                    break
                else:
                    curScore -= 1
                    power += tokens[r]
                    r-=1
            else:
                curScore += 1
                power -= tokens[l]
                l+=1

            maxPossibleScore = max(maxPossibleScore, curScore)
        return maxPossibleScore


s = Solution()

# [100]
# 50
# [200,100]
# 150
# 
# 200
print(s.bagOfTokensScore([100,200,300,400], 200))