class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        need = 0
        
        for c in s:
            if c == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    need+=1
        
        return need+len(stack)