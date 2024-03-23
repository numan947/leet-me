from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower()
        words = paragraph.split(" ")
        banned = set(banned)
        wc = {}
        mx = 0
        res = ""
        for w in words:
            if w not in banned and w:
                wc[w] = wc.get(w, 0) + 1  
                if wc[w]>mx:
                    mx = wc[w]
                    res = w
        return res

s = Solution()

print(s.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
# print(s.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))