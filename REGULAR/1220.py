class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = (1e9+7)
        @cache
        def countStrings(n, curChar):
            if n == 0:
                return 1
            cnt = 0
            if curChar == 'a':
                cnt += countStrings(n-1, 'e')
                cnt%=MOD
            elif curChar == 'e':
                cnt+= countStrings(n-1, 'a')
                cnt+= countStrings(n-1, 'i')
                cnt%=MOD
            elif curChar == 'i':
                cnt+=countStrings(n-1, 'a')
                cnt+=countStrings(n-1, 'e')
                cnt+=countStrings(n-1, 'o')
                cnt+=countStrings(n-1, 'u')
                cnt%=MOD
            elif curChar == 'o':
                cnt+=countStrings(n-1, 'i')
                cnt+=countStrings(n-1, 'u')
                cnt%=MOD
            elif curChar == 'u':
                cnt += countStrings(n-1, 'a')
                cnt%=MOD
            cnt%=MOD
            return cnt
        
        ans = 0
        for c in ['a','e', 'i','o','u']:
            ans += (countStrings(n-1, c))%MOD
        
        return int(ans%MOD)
                