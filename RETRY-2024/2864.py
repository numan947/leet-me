class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c1 = 0
        ans = []
        for i in range(len(s)):
            ans.append('0')
            if s[i] == '1':
                c1 += 1
        ans[-1] = '1'
        c1-=1
        
        i = 0
        while c1:
            ans[i] = '1'
            i+=1
            c1-=1
        return ''.join(ans)
        






if __name__ == '__main__':
    s = Solution()
    print(s.maximumOddBinaryNumber("010"))