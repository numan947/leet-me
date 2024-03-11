class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return "0"
        
        stack = []
        for c in num:
            while k>0 and stack and stack[-1]>c:
                stack.pop()
                k-=1
            stack.append(c)
        
        while stack and k: # make sure we have popped at least k digits
            stack.pop()
            k-=1
        
        stack.reverse()
        while stack and stack[-1] == '0': # removes leading 0s
            stack.pop()
        stack.reverse()
        if not stack:
            return "0"
        res = ''.join(stack)
        return res