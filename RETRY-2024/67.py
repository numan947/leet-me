class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b)>len(a):
            a,b = b, a # a is larger, b is smaller
        b = '0'*(len(a)-len(b))+b
        res = []
        
        c = '0'
        for i in range(len(a)-1, -1, -1):
            
            if a[i] == '0' and b[i] == '0' and c == '0':
                res.append('0')
                c = '0'
            elif a[i] == '0' and b[i] == '0' and c == '1':
                res.append('1')
                c = '0'
            elif a[i] == '0' and b[i] == '1' and c == '0':
                res.append('1')
                c='0'
            elif a[i] == '0' and b[i] == '1' and c == '1':
                res.append('0')
                c='1'
            elif a[i] == '1' and b[i] == '0' and c == '0':
                res.append('1')
                c = '0'
            elif a[i] == '1' and b[i] == '0' and c == '1':
                res.append('0')
                c='1'
            elif a[i] == '1' and b[i] == '1' and c == '0':
                res.append('0')
                c='1'
            elif a[i] == '1' and b[i] == '1' and c == '1':
                res.append('1')
                c='1'
        
        if c == '1':
            res.append('1')
        
        res.reverse()
        return "".join(res)

s = Solution()
print(s.addBinary("1010", "1011"))