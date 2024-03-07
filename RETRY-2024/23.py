# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  
        minHeap = [] #will contain (value, listIdx, listPtr)
        
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(minHeap, (l.val, i, l))
        head = ListNode() # dummy node
        cur = head
        
        while minHeap:
            curItem = heapq.heappop(minHeap)
            
            
            cur.next = curItem[2]
            cur = cur.next
            
            tmp = curItem[2].next
            curItem[2].next = None
            if tmp:
                heapq.heappush(minHeap, (tmp.val,curItem[1],tmp))
        
        return head.next

