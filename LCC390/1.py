class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = r = 0
        wMap = {}
        ans = 0
        # print(len(s))
        while r<len(s):
            c = s[r]
            wMap[c] = wMap.get(c, 0) + 1
            
            while l<=r and wMap[c]>2:
                t = s[l]
                wMap[t]-=1
                if wMap[t] == 0:
                    wMap.pop(t)
                l+=1
            # print(l,)
            ## check if everything ok
            ans = max(ans, r - l+1)
            r += 1
        return ans


s = Solution()
print(s.maximumLengthSubstring("bcbbbcba"))
print(s.maximumLengthSubstring( "adaddccdb"))