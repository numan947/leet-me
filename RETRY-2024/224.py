class Solution:
    def calculate(self, s: str) -> int:
        answer = 0
        sign = 1
        stk = []
        curNum = 0
        
        for c in s:
            if c == ' ': # ignore white space
                continue
            elif ord(c)>=ord('0') and ord(c)<=ord('9'):
                curNum = (10*curNum) + (ord(c)-ord('0'))
            elif c == '+' or c =='-':
                answer += (sign*curNum)
                # reset curNum
                curNum = 0
                if c == '-':
                    sign = -1
                else:
                    sign = 1
            elif c == '(':
                stk.append((answer, sign))
                answer = 0
                curNum = 0
                sign = 1
            elif c== ')':
                answer += (sign * curNum)
                oldAns, oldsign = stk[-1]
                stk.pop()
                answer = (oldsign*answer)
                answer = oldAns + answer
                curNum = 0
                sign = 1
        
        if curNum>0:
            answer += (sign * curNum)
        
        return answer


s = Solution()

print(s.calculate("-(-2)+4"))
print(s.calculate("1   +   1"))
print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 23