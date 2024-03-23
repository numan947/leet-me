class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = (n*(n+1)) // 2
        runningSum = 0
        
        # for i in range(1, n+1):
        #     runningSum+=i
        #     if runningSum == (totalSum-runningSum+i):
        #         return i
        # return -1
        
        lo = 1
        hi = n+1
        tc = 0
        while lo<=hi:
            mid = lo + (hi-lo)//2
            leftSum = mid*(mid+1)//2
            rightSum = totalSum-leftSum + mid
            tc+=1
            if leftSum == rightSum:
                return mid
            if leftSum > rightSum:
                hi = mid - 1
            else:
                lo = mid + 1
        
        return -1



s = Solution()
print(s.pivotInteger(8))
print(s.pivotInteger(1))
print(s.pivotInteger(4))