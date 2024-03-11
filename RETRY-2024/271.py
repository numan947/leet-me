from curses.ascii import isdigit
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            rl = len(s)
            res += f"{rl}$"+s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        cur = 0
        while cur<len(s):
            rl = 0
            while s[cur].isdigit():
                rl*=10
                rl+=ord(s[cur]) - ord('0')
                cur+=1
            
            # assert s[cur] == '$'
            cur+=1 # skip the $
            
            res.append(s[cur:cur+rl])
            cur+=rl
        return res

s = Solution()

enc = s.encode(["ABC","DEF"])
print(s.decode(enc))