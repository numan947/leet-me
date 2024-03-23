class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        posMap = []
        for i, cc in enumerate(s):
            if cc == c:
                posMap.append(i)
        cnt = 0
        
        return (len(posMap)*(len(posMap)+1))//2


s = Solution()

print(s.countSubstrings(s = "abada", c = "a"))
            