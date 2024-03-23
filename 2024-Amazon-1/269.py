from collections import defaultdict, deque
from heapq import heapify
import heapq
from typing import List


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        adjList = {}
        inCount = {}
                
        for w1 in words:
            for c in w1:
                adjList[c] = set()
                inCount[c] = 0

        def checkAndAdd(w1, w2):
            for p in range(min(len(w1), len(w2))):
                if w1[p]!=w2[p]:
                    adjList[w1[p]].add(w2[p])
                    return

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            if len(w1)>len(w2) and w2 == w1[:len(w2)]: # prefix check ==> should check greater than NOT >=
                return ""
            checkAndAdd(w1, w2)

        ## Primary issue was using a list instead of set for building the adjacency list
        ## Second important issue was updating indegree count...it'll be in accurate if we update it during graph building
        ## instead update it later
        
        for u in adjList:
            for v in adjList[u]:
                inCount[v]+=1
        

        
        dq = []
        
        
        for k in inCount.keys():
            if inCount[k] == 0:
                dq.append(k)
        heapq.heapify(dq)
        res = ""
        while dq:
            tmp = heapq.heappop(dq)
            res+=tmp
            
            for n in adjList[tmp]:
                inCount[n]-=1
                if inCount[n] == 0:
                    heapq.heappush(dq, n)
        
        if len(res) != len(inCount.keys()): ## third issue
            return ""
        
        return res
        
    
    
s = Solution()

print(s.alien_order(["wrt","wrf","er","ett","rftt"]))