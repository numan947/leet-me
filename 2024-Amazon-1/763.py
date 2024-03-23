from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # res = []
        # start = {}
        # end = {}
        
        # for i, c in enumerate(s):
        #     if c not in start:
        #         start[c] = i
        #     end[c] = i
        # intervals = set()
        
        # # create intervals
        # for c in s:
        #     intervals.add((start[c], end[c]))
        
        # lst = list(intervals)
        # lst.sort()
        
        # # merge intervals
        
        # curE = lst[0][1]
        # curS = lst[0][0]
        # cur = 1
        
        # while cur<len(lst):
        #     nxtS = lst[cur][0]
        #     nxtE = lst[cur][1]
            
        #     if nxtS < curE:
        #         curE = max(nxtE, curE)
        #     else:
        #         res.append(curE-curS+1)
        #         curE = nxtE
        #         curS = nxtS
        #     cur+=1
        
        # res.append(curE-curS+1)
        # return res
        
        res = []
        end = {}
        for i, c in enumerate(s):
            end[c] = i
        
        curS = 0
        curE = end[s[0]]
        cur = 1
        
        while cur<len(s):
            if cur <= curE:# so there's an overlap
                curE = max(curE, end[s[cur]])
            else: # there's no overlap
                res.append(curE-curS+1)
                curS = cur
                curE = end[s[cur]]
            cur+=1
        res.append(curE-curS+1)
        return res
        


s = Solution()

print(s.partitionLabels(s = "ababcbacadefegdehijhklij"))