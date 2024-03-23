# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy1 = ListNode()
        dummy2 = ListNode()
        dummy1.next = list1
        dummy2.next = list2
        
        # get the end of the list2
        list2End = list2
        while list2End.next:
            list2End = list2End.next
        
        # get the prevA node and prevB node
        prevA = dummy1
        prevB = dummy2
        cur = 0
        
        tmp = dummy1.next
        b+=1 # Make sure we are also counting the end of the node
        
        while tmp:
            if a:
                prevA = tmp
                a-=1
            if b:
                prevB = tmp
                b-=1
            if not a and not b:
                break
            tmp = tmp.next
        
        BNode = prevB.next
        prevB.next = None # disconnect
        prevA.next = None # disconnect
        
        prevA.next = dummy2.next
        list2End.next = BNode
        
        return dummy1.next
                