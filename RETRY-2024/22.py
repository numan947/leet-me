from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        tmpRes = []
        def generate(o, c):
            if o == 0 and c == 0:
                result.append(''.join(tmpRes))
                return
            
            if o<c:
                tmpRes.append(")")
                generate(o, c-1)
                tmpRes.pop()
            if o>0:
                tmpRes.append("(")
                generate(o-1, c)
                tmpRes.pop()
        
        generate(n,n)
        return result

s = Solution()

print(s.generateParenthesis(4))