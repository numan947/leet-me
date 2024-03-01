import heapq
from typing import List


class Solution:
    # def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    #     dp = [0] * len(nums)
    #     dp[0] = nums[0]
    #     for i in range(1, len(nums)):
    #         dp[i] = nums[i]
    #         for j in range(max(i-k, 0), i):
    #             dp[i] = max(dp[i], nums[i]+dp[j])

    #     return max(dp)
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = nums[0]
        max_heap = [(-nums[0], 0)]
        heapq.heapify(max_heap)

        for i in range(1, len(nums)):

            while (len(max_heap)>0 and (i - max_heap[0][1]) > k):
                heapq.heappop(max_heap)

            cur_max = nums[i]
            if len(max_heap)>0:
                cur_max = max(cur_max, nums[i] - max_heap[0][0])
            
            res = max(cur_max, res)
            heapq.heappush(max_heap, (-cur_max, i))

        return res
