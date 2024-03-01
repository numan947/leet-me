from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in ['+', '-', '*','/']:
                v2 = stack.pop()
                v1 = stack.pop()
                
                if t == '+':
                    stack.append(v1+v2)
                elif t == '-':
                    stack.append(v1-v2)
                elif t == '*':
                    stack.append(v1*v2)
                else:
                    sign = +1
                    v1s = -1 if v1<0 else +1
                    v2s = -1 if v2<0 else +1
                    sign = v1s*v2s
                    
                    div = abs(v1)//abs(v2)
                    stack.append(int(div*sign))
            else:
                stack.append(int(t))
            
            # print(stack)
        
        return stack[-1]