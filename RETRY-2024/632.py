from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        flattened = []
        for i, arr in enumerate(nums):
            for v in arr:
                flattened.append((v, i)) # i is the list id
        flattened.sort()
        ansS = float('-inf')
        ansE = float('-inf')
        
        # Now it's just minimum window substring: where the substring is the different lists
        listsInCurrentWindow = {} # count number of items of each list in the current window, need at least one
        listsInWindowSet = set()
        
        l = r = 0
        
        while r<len(flattened):
            curVal, curListId = flattened[r]
            
            listsInCurrentWindow[curListId] = listsInCurrentWindow.get(curListId, 0) + 1
            listsInWindowSet.add(curListId)
            
            while l<r and len(listsInWindowSet) == len(nums):
                tS = flattened[l][0]
                tE = flattened[r][0]
                if (ansS == float('-inf') and ansE == float('-inf')) or (ansE-ansS)>(tE-tS):
                    ansS = tS
                    ansE = tE
                listsInCurrentWindow[flattened[l][1]]-=1
                if listsInCurrentWindow[flattened[l][1]]==0:
                    listsInWindowSet.remove(flattened[l][1])
                l+=1
            r+=1
        
        if ansS == float('-inf'):
            ansS = flattened[0][0]
            ansE = flattened[0][0]
        
        return [ansS, ansE]


s = Solution()

print(s.smallestRange(nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))
print(s.smallestRange([[1,2,3],[1,2,3],[1,2,3]]))