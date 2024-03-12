# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 1:
            return head
        dummy = ListNode()
        dummy.next = head
        def printList(lst):
            while lst:
                print(f"{lst.val}", end="->")
                lst = lst.next
            print("null")
            
        def reverseList(lst, k):
            tmpK = k
            tmpLst = lst
            while tmpK and tmpLst:
                tmpK-=1
                tmpLst = tmpLst.next
            if tmpK:
                return lst, None, None
            ## Only reverse if we at least have k nodes
            hh = dummy = ListNode()
            tail = lst
            while k and lst:
                hhNxt = hh.next
                lstNxt = lst.next
                hh.next = lst
                lst.next = hhNxt
                lst = lstNxt
                k-=1
            return dummy.next, tail, lst
        
        newList = None
        newListTail = None
        cur = head
        while cur:
            tmpHead, tmpTail, nextNode = reverseList(cur, k)
            if not newList:
                newList = tmpHead
            else:
                newListTail.next = tmpHead
            newListTail = tmpTail                
            cur = nextNode
        return newList
    
    
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()

print(s.reverseKGroup(head, 3))
print(s.reverseKGroup(head, 2))