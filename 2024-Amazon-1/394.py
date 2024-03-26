class Solution:
    def decodeString(self, s: str) -> str:
		## Rercursive Solution
  
        p = 0
        def decodeRec():
            nonlocal p
            mult = 0
            resString = ""
            while p<len(s):
                while p<len(s) and s[p].isdigit():
                    mult*=10
                    mult+=ord(s[p]) - ord('0')
                    p+=1
                if s[p] == '[':
                    p+=1
                    tmpRes = decodeRec()
                    resString += mult*(tmpRes)
                    mult = 0
                elif s[p] == ']':
                    p+=1
                    return resString
                else:
                    resString+=s[p]
                    p+=1
            return resString
        return decodeRec()
        
        
        ## Stack with iterative solution
        
        stack = []
        mult = 0
        curString = ""
        p = 0
        
        while p<len(s):
            while p<len(s) and s[p].isdigit():
                mult*=10
                mult+=ord(s[p]) - ord('0')
                p+=1
            
            if s[p] == '[':
                # start of recursive step
                # we save the string where we will add the resultant string, mult is the multiplier to be applied
                stack.append((curString, mult))
                mult = 0
                curString = ""
                p+=1
            elif s[p] == ']':
                # Recruse back
                tmpString, tmpMult = stack.pop()
                tmpString += (tmpMult*curString)
                curString = tmpString
                p+=1
            else:
                curString += s[p]
                p+=1
        
        return curString

s = Solution()
print(s.decodeString("3[a]2[bc]"))
print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))