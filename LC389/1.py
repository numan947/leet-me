class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        r = s[::-1]
        
        for i in range(len(s)-1):
            for j in range(len(r)-1):
                if s[i:i+2] == r[j:j+2]:
                    return True
        return False


s = Solution()

print(s.isSubstringPresent( "leetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcodeleetcode"))
print(s.isSubstringPresent("abcba"))