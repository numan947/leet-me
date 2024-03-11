
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        forward_res = 0
        backward_res = 0
        
        curOpn = 0
        curCls = 0
        
        for i in range(len(s)):
            if s[i] == ')':
                curCls += 1
            else:
                curOpn += 1
            
            if curOpn == curCls:
                forward_res = (curOpn+curCls)
                ans = max(forward_res, ans)
            elif curCls>curOpn: ## not well formed anymore
                curOpn = 0
                curCls = 0
                forward_res = 0
        
        curOpn = 0
        curCls = 0
        backward_res = 0
        
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                curCls += 1
            else:
                curOpn += 1
            
            if curOpn == curCls:
                backward_res = (curOpn+curCls)
                ans = max(backward_res, ans)
            elif curCls<curOpn: ## not well formed anymore
                curOpn = 0
                curCls = 0
                backward_res = 0
        
        return ans

s = Solution()

print(s.longestValidParentheses("(()"))
print(s.longestValidParentheses(")()())"))
print(s.longestValidParentheses("()(()"))