from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        
        cur = len(temperatures)-1
        
        while cur>=0:
            # print(stack)
            while stack and stack[-1][0]<=temperatures[cur]:
                stack.pop()
            
            if stack:
                _,pos = stack[-1]
                ans[cur] = (pos-cur)
            stack.append((temperatures[cur], cur))
            cur -= 1
            
        return ans
    

s = Solution()



print(s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
print(s.dailyTemperatures([30,40,50,60]))
print(s.dailyTemperatures([30,60,90]))