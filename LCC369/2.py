from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zc1, zc2 = 0, 0
        sum1, sum2 = 0, 0
        
        for n in nums1:
            if n == 0:
                zc1+=1
            sum1 += n
        for n in nums2:
            if n == 0:
                zc2+=1
            sum2 += n
        
        
        # print(sum1, zc1)
        # print(sum2, zc2)
        effectiveSum1 = sum1 + zc1
        effectiveSum2 = sum2 + zc2
        
        if effectiveSum1 == effectiveSum2:
            return effectiveSum2
        
        # print(effectiveSum1)
        # print(effectiveSum2)
        
        if effectiveSum1 > effectiveSum2:
            dif = effectiveSum1 - sum2
            if zc2 and dif>=zc2:
                return effectiveSum1
        else:
            dif = effectiveSum2 - sum1
            # print(zc1, dif)
            if zc1 and dif>=zc1:
                return effectiveSum2
        
        return -1


s = Solution()

#184
print(s.minSum([0,22,0,28,2,30,28,0,21,0,20,23,3,1], [0,16,6,17,21,25,26,19,11,10,2,0,29]))