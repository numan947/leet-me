from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        for i,n in enumerate(nums):
            missing ^= ((1+i)^n) # XOR ALL OF THE ELEMENTS BETWEEN [0....n] with ALL OF THE ELEMENT OF THE ARRAY TO FIND THE MISSING
        return missing