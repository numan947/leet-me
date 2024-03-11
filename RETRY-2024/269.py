from collections import deque
from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {}
        inDegree = {}
        for word in words:
            for c in word:
                adjList[c] = set() # create a node for each character in the list of words
                inDegree[c] = 0
        # build the graph
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLen = min(len(w1), len(w2))
            
            if len(w1)>len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            for p in range(minLen):
                if w1[p]!=w2[p]:
                    adjList[w1[p]].add(w2[p])
                    break
        
        for u in adjList.keys():
            for v in adjList[u]:
                inDegree[v] += 1
        
        dq = deque()
        
        for c in inDegree.keys():
            if inDegree[c] == 0:
                dq.append(c)
        
        # print(inDegree)
        res = ""
        
        while dq:
            # print(dq)
            cur = dq.popleft()
            res += cur
                
            for n in adjList[cur]:
                inDegree[n]-=1
                if inDegree[n] == 0:
                    dq.append(n)
        
        if len(res)!=len(inDegree.keys()):
            return ""
        return res

s = Solution()

print(s.foreignDictionary( ["hrn","hrf","er","enn","rfnn"]))
print(s.foreignDictionary(["aaaab","aaabb","aabbb","abbbb","bbbbb","bbbbc","bbccc","bcccc","ccccc","cccdd","ccddd","cdddd","ddddd","ddeee","deeee","eeeee","eeeef","eefff","effff","fffff","ffffg","ffggg","fgggg","ggggg"]))
print(s.foreignDictionary(["ab","ac","ad","ae","af","ag","ah","ai","aj","ak","al","am","an","ao","ap","aq","ar","as","at","au","av","aw","ax","ay","az","ba","bb","bc","bd","be","bf","bg","bh","bi","bj","bk","bl","bm","bn","bo","bp","bq","br","bs","bt","bu","bv","bw","bx","by","bz"]))