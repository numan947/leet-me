from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPal(w, s, e):
            # print(len(w), s, e)
            while s<e:
                if w[s]!=w[e]:
                    return False
                s+=1
                e-=1
            return True
        
        
        N = len(words)
        output = []
        
        lookup = {w:i for i,w in enumerate(words)}
        
        for i in range(N):
            w = words[i]
            if w == "":
                for j in range(N):
                    if i!=j and isPal(words[j], 0, len(words[j])-1):
                        output.append([i,j])
                        output.append([j,i])
                continue
            if w[::-1] in lookup and lookup[w[::-1]]!=i:
                output.append([i,lookup[w[::-1]]])
                
            for k in range(1, len(w)):
                if isPal(w, 0, k-1) and w[k:][::-1] in lookup:
                    output.append([lookup[w[k:][::-1]], i])
                
                if isPal(w, k, len(w)-1) and w[:k][::-1] in lookup:
                    output.append([i, lookup[w[:k][::-1]]])
        
        return output


s = Solution()

print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))