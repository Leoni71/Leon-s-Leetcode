# Recursion
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# Iteration        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        ptr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                ptr.next = ListNode(l2.val)
                l2 = l2.next
            ptr = ptr.next
        
        ptr.next = l1 or l2
        
        return dummy.next
