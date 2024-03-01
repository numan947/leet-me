class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalnum(c):
            t = ord(c)
            return (t>=ord('a') and t<=ord('z')) or (t>=ord('A') and t<=ord('Z')) or (t>=ord('0') and t<=ord('9'))
                
        l,r = 0,len(s)-1
        
        while(l<r):
            while l<r and not isalnum(s[l]):
                l+=1
            while l<r and not isalnum(s[r]):
                r-=1
            if l<r:
                if s[l].lower() != s[r].lower():
                    return False
                l+=1
                r-=1
        
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))