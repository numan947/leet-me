class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digitSum = 0
        tmp = x
        while tmp>0:
            digitSum += (tmp%10)
            tmp//=10
        
        if x%digitSum == 0:
            return digitSum
        return -1