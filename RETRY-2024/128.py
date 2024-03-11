from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seenMap = set(nums)
        longest = 0
        
        for n in seenMap: # well we don't even need to go through the entire list, as we don't care about duplicates
            if n-1 not in seenMap:
                t = n+1
                while t in seenMap:
                    t+=1
                longest = max(longest, t-n)
        return longest
