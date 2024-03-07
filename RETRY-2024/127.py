from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList= {}
        dist = {}
        visited = set()
        
        if endWord not in wordList:
            return 0
        
        def addEdge(w1, w2):
            maxDiff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    maxDiff+=1
            return maxDiff == 1 
        
        ## Build the graph
        adjList[beginWord] = []
        for i in range(len(wordList)):
            if wordList[i] not in adjList:
                adjList[wordList[i]] = []            
            if addEdge(wordList[i], beginWord):
                adjList[wordList[i]].append(beginWord)
                adjList[beginWord].append(wordList[i])
            for j in range(i+1, len(wordList)):
                if wordList[j] not in adjList:
                    adjList[wordList[j]] = []
                if addEdge(wordList[i], wordList[j]):
                    adjList[wordList[i]].append(wordList[j])
                    adjList[wordList[j]].append(wordList[i])
        
        ## Now bfs
        
        dq = deque()
        
        dq.append(beginWord)
        dist[beginWord] = 1
        
        while dq:
            cur = dq.popleft()
            if cur == endWord:
                return dist[endWord]
            
            for nxt in adjList[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    dist[nxt] = dist[cur] + 1
                    dq.append(nxt)
                    
        return 0
    

s = Solution()

print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))