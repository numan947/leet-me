class Solution:
    def countHomogenous(self, s: str) -> int:
        if(len(s) == 1):
            return 1
        
        total = 0
        
        currentStreak = 1
        
        MOD = 1e9+7
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                currentStreak+=1
            else:
                total += (currentStreak*(currentStreak+1))//2
                total%=MOD
                currentStreak = 1
        
        total += (currentStreak*(currentStreak+1))//2
        total%=MOD
        
        
        return total