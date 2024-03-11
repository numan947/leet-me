from curses.ascii import isalpha, isdigit


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        idx = 0
        while idx<len(s):
            while idx<len(s) and s[idx]!="]":
                stack.append(s[idx])
                idx+=1
            
            ## this is in case we are done
            if idx>=len(s) or s[idx]!="]":
                continue
            
            # here s[idx]=="]", so we will pop until we get a "[" and some numbers
            tmpStr = ""
            while stack and stack[-1]!="[":
                tmpStr = stack[-1] + tmpStr
                stack.pop()
            # pop the "["
            stack.pop()
            
            # now stack should have some numers
            num = ""
            while stack and stack[-1].isdigit():
                num = stack[-1] + num
                stack.pop()
            stack.append(int(num)*tmpStr)
            idx+=1
        return ''.join(stack)
        
s = Solution()
print(s.decodeString("3[a]2[bc]"))
print(s.decodeString("2[abc]3[cd]ef"))
print(s.decodeString( "3[a2[c]]"))
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))