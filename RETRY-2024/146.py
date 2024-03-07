class DLLNode:
    def __init__(self,k = -100, v=-100):
        self.v = v
        self.k = k
        self.prv = None
        self.nxt = None


class LRUCache:
    
    def addToList(self, node:DLLNode):
        # adding to the rightmost of the list
        # get to the last item
        lastNode:DLLNode = self.dummyTail.prv
        lastNode.nxt = node
        self.dummyTail.prv = node
        
        node.prv = lastNode
        node.nxt = self.dummyTail
        
    def removeFromList(self, node:DLLNode):
        nxtNode:DLLNode = node.nxt
        prvNode:DLLNode = node.prv
        ## adjust the nxtNode and prvNode's pointers
        prvNode.nxt = nxtNode
        nxtNode.prv = prvNode
        
        ## fix the node
        node.nxt = None
        node.prv = None
    
    def __init__(self, capacity: int):
        self.dummyHead:DLLNode = DLLNode()
        self.dummyTail:DLLNode = DLLNode()
        self.dummyHead.nxt = self.dummyTail
        self.dummyTail.prv = self.dummyHead
        
        self.lookupMap:dict = {}
        self.capacity:int = capacity
        self.currentSize:int = 0
        
    def get(self, key: int) -> int:
        if key in self.lookupMap.keys():
            # move this item to the rightmost of the list
            node:DLLNode = self.lookupMap[key]
            self.removeFromList(node)
            self.addToList(node)
            # return the value
            return node.v
        
        return -1
    
    def removeLRU(self):
        self.currentSize -= 1
        lruNode = self.dummyHead.nxt
        self.removeFromList(lruNode)
        del self.lookupMap[lruNode.k]

    def put(self, key: int, value: int) -> None:
        if key in self.lookupMap.keys():
            # move this item to the rightmost of the list
            node:DLLNode = self.lookupMap[key]
            self.removeFromList(node)
            self.addToList(node)
            node.v = value
        else:
            if self.capacity == self.currentSize:
                self.removeLRU()
            node = DLLNode(key, value)
            self.addToList(node)
            self.lookupMap[key] = node
            self.currentSize += 1

# Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(2)
# param_1 = obj.get(key)
# obj.put(key,value)
lRUCache.put(1, 1);# // cache is {1=1}
lRUCache.put(2, 2); #// cache is {1=1, 2=2}
lRUCache.get(1);    #// return 1
lRUCache.put(3, 3); #// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    ##// returns -1 (not found)
lRUCache.put(4, 4); #// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    #// return -1 (not found)
lRUCache.get(3);    #// return 3
lRUCache.get(4);    #// return 4
