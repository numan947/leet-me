from curses.ascii import isdigit, isspace

from numpy import sign


class Solution:
    def calculate(self, s: str) -> int:
        curSign = +1
        curNum = 0
        stack = []
        result = 0
        
        p = 0 # pointer
        
        while p<len(s):
            curChar = s[p]
            
            if curChar.isdigit():
                curNum *= 10
                curNum += ord(curChar) - ord('0')
            elif curChar == '+' or curChar == '-':
                result += (curSign*curNum)
                
                if curChar == '-':
                    curSign = -1
                else:
                    curSign = 1
                curNum = 0
            elif curChar == '(':
                # update the result
                stack.append((curSign, result)) # store the so far computed result
                # reset these variables for the parenthesis part
                result = 0
                curNum = 0
                curSign = 1
            elif curChar == ')':
                result += (curSign * curNum) # update the result inside the parenthesis
                tmpSign, tmpRes = stack.pop() # restoring start
                tmpRes += (tmpSign * result)
                
                result = tmpRes
                curSign = +1
                curNum = 0
            p+=1
        
        result += (curNum * curSign)
        
        return result


s = Solution()

print(s.calculate(" 2-1 + 2 "))
print(s.calculate(s = "(1+(4+5+2)-3)+(6+8)"))