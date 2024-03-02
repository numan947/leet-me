from typing import List


class Solution:
    # def trap(self, height: List[int]) -> int:
    #     lMax = [0]*len(height)
    #     rMax = [0]*len(height)
    #     lm = 0
    #     for i in range(len(height)):
    #         lMax[i] = lm
    #         lm = max(lm, height[i])
    #     rm = 0
    #     for i in range(len(height)-1, -1, -1):
    #         rMax[i] = rm
    #         rm = max(rm, height[i])
    #     total = 0
    #     for i in range(1, len(height)-1):
    #         mxCap = min(rMax[i], lMax[i])
    #         total += max(mxCap-height[i], 0)
    #     return total

    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ## Idea: whichever one is smaller between leftMax and rightMax determines the amount of water trapped in the location
        lMax, rMax = height[0], height[-1]
        ans = 0
        while l<r:
            if lMax < rMax:
                l+=1 ## cleverly skipping the 0th element
                lMax = max(lMax, height[l])
                ans += (lMax - height[l])
            else:
                r-=1 # cleverly skipping the last element
                rMax = max(rMax, height[r])
                ans += (rMax - height[r])
        
        return ans
    
s = Solution()

print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))