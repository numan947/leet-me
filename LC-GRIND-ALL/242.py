class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mps = {}
        mpt = {}
        for a in s:
            mps[a] = mps.get(a, 0)+1
        for a in t:
            mpt[a] = mpt.get(a, 0)+1
        if len(mps)!=len(mpt):
            return False
        for t in mps:
            if mps.get(t, 0) != mpt.get(t, 0):
                return False
        return True
        