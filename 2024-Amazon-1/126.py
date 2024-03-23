from collections import defaultdict, deque
from typing import List



class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        adjList = {}
        
        def addEdge(w1, w2):
            if w1 == w2:
                return False
            if len(w1)==len(w2):
                diffCnt = 0
                for i in range(len(w1)):
                    if w1[i] != w2[i] and diffCnt>0:
                        return False
                    elif w1[i]!=w2[i]:
                        diffCnt+=1
                return True
            return False
        for i in range(len(wordList)):
            u = wordList[i]
            if u not in adjList:
                adjList[u] = []
            for j in range(i+1, len(wordList)):
                v = wordList[j]
                if v not in adjList:
                    adjList[v] = []
                
                if addEdge(u, v):
                    adjList[u].append(v)
                    adjList[v].append(u)
        if beginWord not in wordList:
            adjList[beginWord] = []
            for w in wordList:
                if addEdge(w, beginWord):
                    adjList[beginWord].append(w)
        
        print(adjList)
        # figure out the minimum length
        minLenth = 0
        dq = deque([beginWord])
        dist = {}
        prev = defaultdict(set)
        dist[beginWord] = 0
        while dq:
            cur = dq.popleft()
            if cur == endWord:
                minLenth = dist[cur]
                break
            for nxt in adjList[cur]:
                # this is the insight, when to add a parent edge
                # add parent when we are discovering the node for the first time
                # or we have visited in some way, but the distance from the cur node to nxt is equal 1 level greater
                if nxt not in dist or dist[nxt] == dist[cur] + 1:
                    prev[nxt].add(cur)
                    if nxt not in dist: 
                        dist[nxt] = dist[cur] + 1
                        dq.append(nxt)

        res = []        
        tmpPath = []
        def dfs(cur):
            if cur == beginWord:
                tmpPath.append(cur)
                res.append(tmpPath[::-1])
                tmpPath.pop()
                return
            if len(tmpPath)>=minLenth:# no more suitable exploration
                return
            tmpPath.append(cur)            
            for p in prev[cur]:
                dfs(p)
            tmpPath.pop()
        dfs(endWord)
        return res

s = Solution()

# print(s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
# print(s.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))

print(s.findLadders("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]))
# print(s.findLadders("aaaaa", "uuuuu", ["aaaaa","waaaa","wbaaa","xaaaa","xbaaa","bbaaa","bbwaa","bbwba","bbxaa","bbxba","bbbba","wbbba","wbbbb","xbbba","xbbbb","cbbbb","cwbbb","cwcbb","cxbbb","cxcbb","cccbb","cccwb","cccwc","cccxb","cccxc","ccccc","wcccc","wdccc","xcccc","xdccc","ddccc","ddwcc","ddwdc","ddxcc","ddxdc","ddddc","wdddc","wdddd","xdddc","xdddd","edddd","ewddd","ewedd","exddd","exedd","eeedd","eeewd","eeewe","eeexd","eeexe","eeeee","weeee","wfeee","xeeee","xfeee","ffeee","ffwee","ffwfe","ffxee","ffxfe","ffffe","wfffe","wffff","xfffe","xffff","gffff","gwfff","gwgff","gxfff","gxgff","gggff","gggwf","gggwg","gggxf","gggxg","ggggg","wgggg","whggg","xgggg","xhggg","hhggg","hhwgg","hhwhg","hhxgg","hhxhg","hhhhg","whhhg","whhhh","xhhhg","xhhhh","ihhhh","iwhhh","iwihh","ixhhh","ixihh","iiihh","iiiwh","iiiwi","iiixh","iiixi","iiiii","wiiii","wjiii","xiiii","xjiii","jjiii","jjwii","jjwji","jjxii","jjxji","jjjji","wjjji","wjjjj","xjjji","xjjjj","kjjjj","kwjjj","kwkjj","kxjjj","kxkjj","kkkjj","kkkwj","kkkwk","kkkxj","kkkxk","kkkkk","wkkkk","wlkkk","xkkkk","xlkkk","llkkk","llwkk","llwlk","llxkk","llxlk","llllk","wlllk","wllll","xlllk","xllll","mllll","mwlll","mwmll","mxlll","mxmll","mmmll","mmmwl","mmmwm","mmmxl","mmmxm","mmmmm","wmmmm","wnmmm","xmmmm","xnmmm","nnmmm","nnwmm","nnwnm","nnxmm","nnxnm","nnnnm","wnnnm","wnnnn","xnnnm","xnnnn","onnnn","ownnn","owonn","oxnnn","oxonn","ooonn","ooown","ooowo","oooxn","oooxo","ooooo","woooo","wpooo","xoooo","xpooo","ppooo","ppwoo","ppwpo","ppxoo","ppxpo","ppppo","wpppo","wpppp","xpppo","xpppp","qpppp","qwppp","qwqpp","qxppp","qxqpp","qqqpp","qqqwp","qqqwq","qqqxp","qqqxq","qqqqq","wqqqq","wrqqq","xqqqq","xrqqq","rrqqq","rrwqq","rrwrq","rrxqq","rrxrq","rrrrq","wrrrq","wrrrr","xrrrq","xrrrr","srrrr","swrrr","swsrr","sxrrr","sxsrr","sssrr","ssswr","sssws","sssxr","sssxs","sssss","wssss","wtsss","xssss","xtsss","ttsss","ttwss","ttwts","ttxss","ttxts","tttts","wttts","wtttt","xttts","xtttt","utttt","uwttt","uwutt","uxttt","uxutt","uuutt","uuuwt","uuuwu","uuuxt","uuuxu","uuuuu","zzzzz","zzzzy","zzzyy","zzyyy","zzyyx","zzyxx","zzxxx","zzxxw","zzxww","zzwww","zzwwv","zzwvv","zzvvv","zzvvu","zzvuu","zzuuu","zzuut","zzutt","zzttt","zztts","zztss","zzsss","zzssr","zzsrr","zzrrr","zzrrq","zzrqq","zzqqq","zzqqp","zzqpp","zzppp","zzppo","zzpoo","zzooo","zzoon","zzonn","zznnn","zznnm","zznmm","zzmmm","zzmml","zzmll","zzlll","zzllk","zzlkk","zzkkk","zzkkj","zzkjj","zzjjj","zzjji","zzjii","zziii","zziih","zzihh","zzhhh","zzhhg","zzhgg","zzggg","zzggf","zzgff","zzfff","zzffe","zzfee","zzeee","zzeed","zzedd","zzddd","zzddc","zzdcc","zzccc","zzccz","azccz","aaccz","aaacz","aaaaz","uuuzu","uuzzu","uzzzu","zzzzu"]))