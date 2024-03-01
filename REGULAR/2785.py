from curses.ascii import SO


class Solution:
    def sortVowels(self, s: str) -> str:
        def isVowel(c):
            return c == 'A' or c == 'E' or c == 'I' or c=='O' or c=='U' or c == 'a' or c == 'e' or c == 'o' or c=='i' or c == 'u'
        
        
        dd = {}
        tr = []
        
        for i, c in enumerate(s):
            if isVowel(c):
               tr.append(i)
               dd[ord(c)] = dd.get(ord(c), 0) + 1
        
        allvowels = list(dd.items())
        allvowels.sort()
        
        print(allvowels)
        
        cur = 0
        
        s = list(s)
        for p in tr:
            if allvowels[cur][1] == 0:
                cur+=1
            s[p] =  chr(allvowels[cur][0])
            newV = allvowels[cur][1] - 1 
            allvowels[cur] = (allvowels[cur][0], newV)

        return ''.join(s)

s = Solution()

print(s.sortVowels("lEetcOde"))