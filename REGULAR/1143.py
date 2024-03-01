class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        def solve(idx1, idx2):
            if(idx1,idx2) in dp:
                return dp[(idx1,idx2)]
            if idx1 == len(text1) or idx2 == len(text2): # no more match
                return 0
            
            mxSeq = 0
            if(text1[idx1] == text2[idx2]):
                dp[(idx1,idx2)] = max(mxSeq, 1+solve(idx1+1, idx2+1))
                return dp[(idx1,idx2)]
            mxSeq = max(mxSeq, solve(idx1+1, idx2))
            mxSeq = max(mxSeq, solve(idx1, idx2+1))
            dp[(idx1,idx2)] = mxSeq
            return mxSeq
        
        return solve(0,0)