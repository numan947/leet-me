# import heapq


# class HeapElem:
#     def __init__(self, val, frq, idx):
#         self.val = val
#         self.frq = frq
#         self.idx = idx
    
#     def __lt__(self, other):
#         if self.frq  == other.frq:
#             return self.idx > other.idx
#         return self.frq > other.frq


# class FreqStack:

#     def __init__(self):
#         self.frqMap = {}
#         self.heap = []
#         self.curSize = 0
        

#     def push(self, val: int) -> None:
#         if val not in self.frqMap:
#             self.frqMap[val] = 0
#         self.frqMap[val] += 1
        
#         heapq.heappush(self.heap, HeapElem(val, self.frqMap[val], self.curSize))
#         self.curSize+=1

#     def pop(self) -> int:
#         elem:HeapElem = heapq.heappop(self.heap)
#         self.frqMap[elem.val]-=1
#         # self.curSize -=1
#         return elem.val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()





class FreqStack:

    def __init__(self):
        self.frq = {}
        self.frqList = {}
        self.curMaxFreq = 0
        

    def push(self, val: int) -> None:
        if val not in self.frq.keys():
            self.frq[val] = 0
        self.frq[val]+=1
        
        if self.frq[val] not in self.frqList.keys():
            self.frqList[self.frq[val]] = []
        self.frqList[self.frq[val]].append(val)
        
        self.curMaxFreq = max(self.curMaxFreq, self.frq[val])

    def pop(self) -> int:
        retVal = self.frqList[self.curMaxFreq].pop()
        self.frq[retVal]-=1
        
        if len(self.frqList[self.curMaxFreq]) == 0:
            self.curMaxFreq -= 1
        return retVal 


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

















