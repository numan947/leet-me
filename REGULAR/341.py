# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []  # list,nextPointerPosition
        self.curList = nestedList
        self.index = 0
        self.findIndexVal()
        print(self.value)
        
    
    def findIndexVal(self):
        while (self.index < len(self.curList)) or self.stack:
            if self.index < len(self.curList):
                curElem = self.curList[self.index]
                if curElem.isInteger():# we are done!!
                    self.value = curElem.getInteger()
                    self.index += 1
                    return
                else:
                    self.stack.append((self.curList, self.index+1))
                    self.curList = self.curList[self.index].getList()
                    self.index = 0
            else:
                self.curList, self.index = self.stack.pop() 
        self.value = None
        
    def next(self) -> int:
        retVal = self.value
        self.findIndexVal()
        return retVal

        # return None

    def hasNext(self) -> bool:
        return self.value is not None
