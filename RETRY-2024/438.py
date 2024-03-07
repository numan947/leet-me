from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        res = []
        wl = len(p)
        pMap = [0]*26
        wMap = [0]*26
        for c in p:
            pMap[ord(c)-ord('a')]+=1
                    
        def mapsEqual():
            for i in range(26):
                if pMap[i]!=wMap[i]:
                    return False
            return True
        
        l = r = 0
        while r<len(p):
            wMap[ord(s[r]) - ord('a')] += 1
            r+=1
        
        if mapsEqual():
            res.append(l)
        
        while r<len(s):
            wMap[ord(s[l]) - ord('a')]-=1
            l+=1
            wMap[ord(s[r]) - ord('a')]+=1
            r+=1
            if mapsEqual():
                res.append(l)
        return res        
        
        

# s = Solution()

# print(s.findAnagrams(s = "cbaebabacd", p = "abc"))