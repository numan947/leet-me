from collections import defaultdict
from typing import Counter, List

from traitlets import default


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        values = list(freq.values())
        values.sort()
        mxElem = values[-1]
        sm = 0
        while values and values[-1] == mxElem:
            sm += mxElem
            values.pop()
        return sm

s = Solution()

print(s.maxFrequencyElements(nums = [1,2,2,3,1,4]))