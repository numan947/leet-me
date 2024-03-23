class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k>=len(num):
            return "0"
        ## Observation: Our final number will be smallest if we can keep the digits
        ## that are in the left side in increasing order
        
        stack = []
        for c in num:
			# this stack will keep the list in increasing order until k digits are deleted
            while stack and k and stack[-1]>c:
                stack.pop()
                k-=1
            stack.append(c)
        
        ## our stack should contain everything in increasing order as possible -> so
        ## the left most parts are as small as possible, if we still have k left, we
        ## should remove from the end to make it smaller
        
        while stack and k:
            stack.pop()
            k-=1
        
        ## our stack can have leading 0s, need to remove them
        stack.reverse()
        while stack and stack[-1] == '0':
            stack.pop()
        stack.reverse()
        
        ## edge case when stack become empty
        if not stack:
            return "0"
        
        # we got the final answer
        return ''.join(stack)        
    
    
s = Solution()
print(s.removeKdigits("1432219", 3))
print(s.removeKdigits(num = "10200", k = 1))
        