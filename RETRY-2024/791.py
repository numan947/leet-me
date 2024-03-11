class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sCount = [0]*26
        for c in s:
            t = ord(c) - ord('a')
            sCount[t]+=1
        
        res = ""
        for tc in order:
            c = ord(tc) - ord('a')
            if sCount[c]>0:
                res += chr(c + ord('a'))*sCount[c]
                sCount[c] = 0
        
        for i in range(26):
            if sCount[i]>0:
                res += chr(i + ord('a'))*sCount[i]
                sCount[i] = 0
        
        return res

s = Solution()

print(s.customSortString(order = "cba", s = "abcd" ))
print(s.customSortString(order = "bcafg", s = "abcd" ))