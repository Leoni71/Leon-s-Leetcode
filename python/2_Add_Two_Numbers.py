# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        ptr = dummy
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            val = s%10
            carry = s//10
            
            ptr.next = ListNode(val)
            
            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry: ptr.next = ListNode(carry)
            
        return dummy.next
