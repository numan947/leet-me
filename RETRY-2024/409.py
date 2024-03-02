class Solution:
    def longestPalindrome(self, s: str) -> int:
        countMap = {}
        for c in s:
            countMap[c] = countMap.get(c, 0) + 1
        
        maxLen = 0
        oddFound = 0
        for k,v in countMap.items():  
            # print(k, v)
            if v%2 == 1:
                maxLen += (v-1) ## NOTE: I always forget that I can take a partial part of the strings
                oddFound = 1
            else:
                maxLen += v
        
        return oddFound + maxLen




s = Solution()
print(s.longestPalindrome("abccccdd"))
print(s.longestPalindrome("a"))