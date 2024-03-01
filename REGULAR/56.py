from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]

        for s, e in intervals[1:]:
            lastEnd = output[-1][1]

            if s <= lastEnd:
                output[-1][1] = max(lastEnd, e)
            else:
                output.append([s, e])

        return output