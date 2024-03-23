from curses.ascii import isdigit, isspace


class Solution:
    def calculate(self, s: str) -> int:
        ## Straight forward Stack solution
        def intDiv(x, y): # returns x//y
            sign = -1 if ((x<0 or y<0 ) and not(x<0 and y<0)) else 1
            res = abs(x)//abs(y)
            return sign*res
        
        # stack = []
        # curOp = '+'
        # curNum = 0
        
        # for c in s:
        #     if c.isspace():
        #         continue
        #     elif c.isdigit():
        #         curNum*=10
        #         curNum+=ord(c)-ord('0')
        #     else:
        #         if curOp == '-' or curOp == '+':
        #             if curOp=='-':
        #                 curNum = -curNum
        #             stack.append(curNum)
        #         elif curOp == '*':
        #             tmp = stack.pop()
        #             stack.append(tmp*curNum)
        #         elif curOp == '/':
        #             tmp = stack.pop()
        #             stack.append(intDiv(tmp, curNum))
        #         curNum = 0
        #         curOp = c
    
        # if curOp == '-' or curOp == '+':
        #         if curOp=='-':
        #             curNum = -curNum
        #         stack.append(curNum)
        # elif curOp == '*':
        #     tmp = stack.pop()
        #     stack.append(tmp*curNum)
        # elif curOp == '/':
        #     tmp = stack.pop()
        #     stack.append(intDiv(tmp, curNum))
        # return sum(stack)
        
        
        ### OPTIMIZED WITHOUT STACK
        
        partialResult = 0 # for storing partialResults
        prevNum = 0
        curNum = 0
        curOp = '+'
        
        for c in s:
            if c.isspace():
                continue
            elif c.isdigit():
                curNum*=10
                curNum+=ord(c)-ord('0')
            else:
                # this is operator territory                
                if curOp == '+' or curOp == '-':
                    if curOp == '-':
                        curNum = -curNum
                    partialResult+= prevNum
                    prevNum = curNum
                elif curOp == '*':
                    prevNum = (prevNum * curNum)
                elif curOp == '/':
                    prevNum = intDiv(prevNum, curNum)
                curNum = 0
                curOp = c
        
        if curOp == '+' or curOp == '-':
            if curOp == '-':
                curNum = -curNum
            partialResult+= prevNum
            prevNum = curNum
        elif curOp == '*':
            prevNum = (prevNum * curNum)
        elif curOp == '/':
            prevNum = intDiv(prevNum, curNum)
        
        
        return partialResult + prevNum
        

s = Solution()

print(s.calculate('3+2*2'))
print(s.calculate(s = " 3+5 / 2 "))
print(s.calculate("14-3/2"))