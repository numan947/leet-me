from typing import List
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        #Core idea: make each node root, and count the possible trees
        arr.sort()
        hashMap = {}
        for i, a in enumerate(arr):
            hashMap[a] = i
        mod = 1e9+7
        
        @cache
        def countTrees(rootValue):
            if rootValue not in hashMap:
                return 0
            
            count = 1        
            for t in arr:
                if rootValue%t == 0 and (rootValue//t) in hashMap.keys():
                    count += (countTrees(t)%mod * countTrees(rootValue//t)%mod)%mod # count should be the number of ways we can make the tree root-> multiplication 
            
            return count

        res = 0
        for p in arr:
            res += countTrees(p)
            res%=mod
        
        return int(res)