from curses.ascii import isdigit


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curNum = 0
        curOp = '+'
        for c in s:
            if c.isspace():
                continue
            if c.isdigit():
                curNum*=10
                curNum += ord(c)-ord('0')
            else:
                if curOp == '+':
                    stack.append(curNum)
                elif curOp == '-':
                    stack.append(-curNum)
                elif curOp == '*':
                    stack.append(stack.pop()*curNum)
                elif curOp == '/':
                    tmp = stack.pop()
                    sign = -1 if tmp<0 else +1
                    tmp = abs(tmp)
                    divRes = tmp//curNum
                    divRes *= sign
                    stack.append(divRes)
                curNum = 0
                curOp = c
        if curOp == '+':
            stack.append(curNum)
        elif curOp == '-':
            stack.append(-curNum)
        elif curOp == '*':
            stack.append(stack.pop()*curNum)
        elif curOp == '/':
            tmp = stack.pop()
            sign = -1 if tmp<0 else +1
            tmp = abs(tmp)
            divRes = tmp//curNum
            divRes *= sign
            stack.append(divRes)
            
        return sum(stack)


s = Solution()

print(s.calculate(s = "3+2*2"))
print(s.calculate('3 / 2'))
print(s.calculate(" 3+5 / 2 "))

print(s.calculate("14-3/2"))