class Solution:
    def longestValidParentheses(self, s: str) -> int:
        validMax = 0
        
        o = 0
        c = 0
        for i in range(len(s)):
            if s[i] == '(':
                o+=1
            else:
                c+=1
            
            if o==c:
                validMax = max(validMax, 2*min(o, c))
            
            if c>o: # not possible to find valid
                c = 0
                o = 0
        o = 0
        c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                o+=1
            else:
                c+=1
            if o==c: # == check because of the substring requirement
                validMax = max(validMax, 2*min(o, c))
            if c>o: # not possible to find valid
                c = 0
                o = 0
        
        return validMax


s = Solution()
print(s.longestValidParentheses(s = "(()"))
print(s.longestValidParentheses(s = ")()())"))
print(s.longestValidParentheses(""))
print(s.longestValidParentheses("()(()"))