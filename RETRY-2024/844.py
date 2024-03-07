class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ## Stack solution
        # s_stack = []
        # t_stack = []
        
        # for c in s:
        #     if c == "#":
        #         if s_stack:
        #             s_stack.pop()
        #     else:
        #         s_stack.append(c)
        
        # for c in t:
        #     if c == "#":
        #         if t_stack:
        #             t_stack.pop()
        #     else:
        #         t_stack.append(c)
        
        # # print(s_stack)
        # # print(t_stack)
        # if len(s_stack)!=len(t_stack):
        #     return False
        
        # for i in range(len(s_stack)):
        #     if s_stack[i]!=t_stack[i]:
        #         return False
        # return True
        
        
        ## Memory Optimizing
        
        def getNextValidIndex(ss, idx):
            backspace = 0
            
            while idx>=0:
                if ss[idx] == '#':
                    backspace+=1
                else:
                    if backspace == 0:
                        return idx
                    else:
                        backspace -=1
                idx -=1
            
            return idx
        
        
        s_idx = len(s)-1
        t_idx = len(t)-1
        
        
        while s_idx>=0 or t_idx>=0:
            vs = getNextValidIndex(s, s_idx)
            ts = getNextValidIndex(t, t_idx)
            
            cs = s[vs] if vs>=0 else ""
            ct = t[ts] if ts>=0 else ""
            
            if cs != ct:
                return False
            s_idx = vs - 1
            t_idx = ts - 1
        
        return True
        

s = Solution()
print(s.backspaceCompare("y#fo##f", "y#f#o##f"))
print(s.backspaceCompare("bbbextm","bbb#extm"))
print(s.backspaceCompare("nzp#o#g", "b#nzp#o#g"))