class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cntR = {}
        cntM = {}
        for c in ransomNote:
            cntR[c] = cntR.get(c, 0) + 1
        for c in magazine:
            cntM[c] = cntM.get(c, 0) + 1
        for c, v in cntR.items():
            if c not in cntM or cntM[c]<v:
                return False
        return True