class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tMap = {}
        for c in t: ## need a counter to make sure we got a match
            tMap[c] = tMap.get(c, 0) + 1
        
        ws, we = 0, 0
        wMap = {}
        matchCount = 0
        ans = float('inf')
        ansL, ansR = 0,0
        
        while we < len(s):
            wMap[s[we]]= wMap.get(s[we], 0) + 1
            if tMap.get(s[we],0) == wMap.get(s[we], 0):
                matchCount += 1
            we+=1
            
            while matchCount == len(tMap):
                if (we-ws+1<ans):
                    ans = we-ws+1
                    ansL = ws
                    ansR = we
                wMap[s[ws]]-=1
                if tMap.get(s[ws],0) >wMap.get(s[ws],0) :
                    matchCount-=1
                ws+=1
        
        
        if ans == float('inf'):
            return ""
        
        print(ansL, ansR)
        return s[ansL:ansR]
    
    

s = Solution()

print(s.minWindow("AB", "A"))