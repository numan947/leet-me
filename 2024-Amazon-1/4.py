from typing import List


"""
1 2 3 4 5 6 7 8
^



"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1) + len(nums2)
        leftSize = N//2
        
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1 # always binary search the shorter array
        
        L, R = 0, len(nums1)-1
        
        while True:
            M = (L+R)//2
            
            ## find the suitable positions on the nums1 and nums2 array
            posInNums1 = M
            posInNums2 = leftSize-(M+1) - 1 # M+1 is the size of the nums1 from 0 ... M, and -1 is for adjusting the pointer in nums2
			
            ## check if we found the answer
            rMostNums1 = nums1[posInNums1] if posInNums1>=0 else float('-inf') #Aleft
            rMostNums2 = nums2[posInNums2] if posInNums2>=0 else float('-inf') #Bleft
            
            lMostNums1 = nums1[posInNums1+1] if (posInNums1+1)<len(nums1) else float('inf') #Aright
            lMostNums2 = nums2[posInNums2+1] if (posInNums2+1)<len(nums2) else float('inf') #Bright
            
            # check if we have found the suitable partition
            if rMostNums1<=lMostNums2 and rMostNums2<=lMostNums1:
                if N%2:
                    return min(lMostNums1, lMostNums2)
                else:
                    return (max(rMostNums1, rMostNums2) + min(lMostNums1, lMostNums2))/2.0
            elif rMostNums1>lMostNums2:
                R = M - 1
            else:
                L = M + 1


s = Solution()

print(s.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))