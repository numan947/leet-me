from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToChar = {
                    "2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"
                }
        
        tmp = []
        def findAll(cur):
            if cur == len(digits):
                if tmp:
                    res.append(''.join(tmp))
                return
            
            for c in digitsToChar[digits[cur]]:
                tmp.append(c)
                findAll(cur+1)
                tmp.pop()
        
        findAll(0)
        return res