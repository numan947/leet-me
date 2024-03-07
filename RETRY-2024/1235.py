from functools import cache
from typing import List
import bisect

class Solution:
    def binarySearch(self, jobs, start, target):
        end = len(jobs)-1
        possible = -1
        while start<=end:
            mid = start + (end-start)//2
            if jobs[mid][0]>=target:
                possible = mid
                end = mid - 1
            else:
                start = mid + 1
        return possible

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        res = 0
        # jobs = []
        # for i in range(len(startTime)):
        #     jobs.append((startTime[i], endTime[i], profit[i]))
        # jobs.sort()
        jobs = sorted(zip(startTime, endTime, profit))
        
        # dp = {}
        @cache
        def findMaxProfit(idx):
            # if idx in dp.keys():
            #     return dp[idx]
            if idx>=len(jobs):
                return 0
            # option 1: skip current job
            profit1 = findMaxProfit(idx+1)
            
            # option2: take the current job and try to maximize
            curEnd = jobs[idx][1]
            profit2 = 0
            # findNext = self.binarySearch(jobs, idx+1, curEnd)
            findNext = bisect.bisect_left(jobs, (jobs[idx][1], -1, -1))
            if findNext>0:
                profit2 = findMaxProfit(findNext)
            
            
            # dp[idx] = max(profit1, profit2+jobs[idx][2])
            return max(profit1, profit2+jobs[idx][2])
        
        res = findMaxProfit(0)
        return res



s = Solution()

print(s.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70])) # 120
print(s.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60])) # 150