# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def findMid(self, lst):
        slow = fast = lst
        slowPrev = None
        while fast and fast.next:
            slowPrev = slow
            slow = slow.next
            fast = fast.next.next
        return slow, slowPrev
    
    def reverse(self, lst):
        head = ListNode()
        
        while lst!=None:
            tmp = head.next
            nxt = lst.next 
            
            head.next = lst
            lst.next = tmp
            lst = nxt
        
        return head.next
        
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        mid, midPrev = self.findMid(head)
        lst2 = mid
        midPrev.next= None
        
        lst2 = self.reverse(lst2)
        while head and lst2:
            if head.val != lst2.val:
                return False
            head = head.next
            lst2 = lst2.next
        
        return True


head = ListNode(1,next=ListNode(2, next=ListNode(2, next=ListNode(1))))

s = Solution()

print(s.isPalindrome(head))