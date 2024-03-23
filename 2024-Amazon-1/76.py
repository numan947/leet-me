from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = defaultdict(int)
        for c in t:
            tMap[c]+=1
        toMatch = len(tMap)
        
        minLength = float('inf')
        ans = (-1, -1)
        l = r = 0
        wMap = defaultdict(int)
        currentMatch = 0
        
        while r<len(s):
            wMap[s[r]] += 1
            
            if wMap[s[r]] == tMap[s[r]]:
                currentMatch += 1
            
            while currentMatch == toMatch and l<=r: # this is the edge
                if minLength == float('inf') or minLength>(r-l+1):
                    # print(l, r)
                    ans = (l, r)
                    minLength = (r-l+1)
                
                c = s[l]
                l+=1
                wMap[c]-=1
                if wMap[c] < tMap[c]:
                    currentMatch-=1
            r+=1
        
        if r-l+1<minLength and currentMatch == toMatch:
            ans = (l, r)
            minLength = (r-l+1)


        if minLength != float('inf'):
            return s[ans[0]:ans[1]+1]
        return ""
    
s = Solution()

print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("ab", "a"))