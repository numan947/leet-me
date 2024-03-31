class Solution:
    def minSwaps(self, s: str) -> int:
        length = len(s)
        oneCount = 0
        zeroCount = 0
        changeNeed1 = 0
        st = 0
        for i in range(length):
            if s[i] == '1':
                oneCount+=1
            else:
                zeroCount += 1
            if st != int(s[i]):
                changeNeed1 += 1
            st = 1 - st
        changeNeed2 = 0
        st = 1
        for i in range(length):
            if st != int(s[i]):
                changeNeed2 += 1
            st = 1 - st
        
        ans = -1
        if len(s)%2 == 0 and  oneCount!=zeroCount:
            return ans
        elif len(s)%2 and ((oneCount-1!=zeroCount) and (zeroCount-1!=oneCount)):
            return ans
        # print(changeNeed1, changeNeed2)
        if changeNeed1%2 == 0 and changeNeed2%2 == 0:
            ans = min(changeNeed1, changeNeed2)
        elif changeNeed2%2 == 0:
            ans = changeNeed2
        elif changeNeed1%2 == 0:
            ans = changeNeed1
        
        if ans == -1:
            return ans
        
        if oneCount>=ans//2 and zeroCount>=ans//2:
            return ans//2
        return -1

s = Solution()
print(s.minSwaps("010"))
# print(s.minSwaps("111000"))
# print(s.minSwaps("1110"))
# print(s.minSwaps("011111"))