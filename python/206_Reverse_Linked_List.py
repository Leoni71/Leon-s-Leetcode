# Recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
       
# Iteration
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            temp = head.next
            head.next = new_head
            head, new_head = temp, head
        
        return new_head
