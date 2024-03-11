class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = r = 0
        wMap = {}
        ans = 0
        while r < len(s):
            wMap[s[r]] = wMap.get(s[r], 0) + 1
            needToReplace = (r-l+1) - (max(wMap.values()))
                        
            while l<r and needToReplace > k:
                wMap[s[l]] = wMap.get(s[l], 0) - 1
                l+=1
                needToReplace = (r-l+1) - (max(wMap.values()))
            r+=1
            ans = max(r-l, ans)

        return ans
            
            
                
s = Solution()

print(s.characterReplacement("ABBB", 2))
print(s.characterReplacement(s = "ABAB", k = 2))
print(s.characterReplacement( s = "AABABBA", k = 1))
print(s.characterReplacement("AABBCABBCAB", 3))
print(s.characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))
print(s.characterReplacement("IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR", 2))