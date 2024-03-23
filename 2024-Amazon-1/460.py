from collections import defaultdict


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1, prev=self.left) # thse are sentinnel/dummy nodes
        self.left.next = self.right
        self.keyToNode = {}
    
    def length(self):
        return len(self.keyToNode)
    
    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.keyToNode[val] = node
        self.right.prev = node
        node.prev.next = node
    
    def pop(self, val):
        if val in self.keyToNode:
            node = self.keyToNode[val]
            next,prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.keyToNode.pop(val, None)
    
    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        self.pop(val)
        self.pushRight(val)




class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.keyValueMap = {}
        self.countMap = defaultdict(int)
        self.listMap = defaultdict(DoublyLinkedList)
    
    def counter(self, key):
        curCount = self.countMap[key]
        self.countMap[key] += 1
        self.listMap[curCount].pop(key)
        self.listMap[curCount+1].pushRight(key)
        
        if curCount == self.lfuCnt and self.listMap[curCount].length() == 0:
            self.lfuCnt+=1

    def get(self, key: int) -> int:
        if key not in self.keyValueMap:
            return -1
        self.counter(key)
        return self.keyValueMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        
        if key not in self.keyValueMap and len(self.keyValueMap) == self.cap:
            res = self.listMap[self.lfuCnt].popLeft()
            self.keyValueMap.pop(res)
            self.countMap.pop(res)
            
        self.keyValueMap[key] = value
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)