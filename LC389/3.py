from collections import defaultdict
from functools import cache


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqMap = defaultdict(int)
        for c in word:
            freqMap[c] += 1
        all_vals = sorted(freqMap.values())
        @cache
        def findMin(sorted_vals):
            if not sorted_vals:
                return 0
            if sorted_vals[-1] - sorted_vals[0]<=k:
                return 0
            toRemoveFromBig = (sorted_vals[-1] - sorted_vals[0]) - k
            tmp = [x for x in sorted_vals]
            tmp[-1] = tmp[-1] - toRemoveFromBig
            tmp.sort()
            return min(sorted_vals[0]+ findMin(tuple(sorted_vals[1:])), toRemoveFromBig + findMin(tuple(tmp)))    
        return findMin(tuple(all_vals))
    
s = Solution()

print(s.minimumDeletions(word = "aabcaba", k = 0))
print(s.minimumDeletions(word = "dabdcbdcdcd", k = 2))
print(s.minimumDeletions( word = "aaabaaa", k = 2))
print(s.minimumDeletions("aaaaaaaaaaaaaaaaaabbbc", k = 2))
print(s.minimumDeletions("vvnowvov", 2))
print(s.minimumDeletions("vnnppvvbbn", 0))