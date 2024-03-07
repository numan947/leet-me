from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToNameMap = {}
        adjList = {}
        nodes = set()
        
        for a in accounts:
            name = a[0]
            for i, e in enumerate(a[1:]):
                emailToNameMap[e] = name
                if e not in adjList.keys():
                    adjList[e] = []
                    nodes.add(e)
                for j, f in enumerate(a[i+1:]):
                    emailToNameMap[f] = name
                    if f not in adjList.keys():
                        nodes.add(f)
                        adjList[f] = []
                    
                    adjList[e].append(f)
                    adjList[f].append(e)
        
        visited = set()
        tmpLst = []
        def dfs(node):
            if node in visited:
                return
            tmpLst.append(node)
            visited.add(node)
            
            for nei in adjList[node]:
                dfs(nei)
            
        result = []
        for n in list(nodes):
            if n in visited:
                continue
            tmpLst.clear()
            dfs(n)
            tmpLst.sort()
            name = emailToNameMap[tmpLst[0]]
            result.append([name]+[x for x in tmpLst])
        
        return result
        


s = Solution()

print(s.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
        
        
        
        
        
        
        
        
        
        