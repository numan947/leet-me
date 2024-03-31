class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # ## Stack solution
        # openParenPositions = [] #stack
        # invalidPositions = set() # list
        
        # for pos, c in enumerate(s):
        #     if c == "(":
        #         openParenPositions.append(pos)
        #     elif c == ")":
        #         if openParenPositions:
        #             openParenPositions.pop()
        #         else:
        #             invalidPositions.add(pos)
        
        # while openParenPositions:
        #     invalidPositions.add(openParenPositions.pop())
        
        # ret = ""
        # for i, c in enumerate(s):
        #     if i not in invalidPositions:
        #         ret += c
        # return ret
        
        
        ## SPACE EFFICIENT SOLUTION
        s = list(s) # convert to list
        openCloseBalance = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                openCloseBalance+=1
            elif s[i] == ')':
                if openCloseBalance:
                    openCloseBalance -= 1
                else:
                    s[i] = '#'
        
        openCloseBalance = 0 # reset
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                openCloseBalance+=1
            elif s[i] == '(':
                if openCloseBalance:
                    openCloseBalance -= 1
                else:
                    s[i] = '#'
        
        res = ""
        for c in s:
            if c!='#':
                res += c
        
        return res


s = Solution()
print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
print(s.minRemoveToMakeValid("))(("))