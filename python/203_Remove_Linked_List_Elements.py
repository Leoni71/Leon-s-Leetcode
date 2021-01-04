class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        prev = dummy
        prev.next, ptr = head, head
        while ptr:
            if ptr.val == val:
                ptr = ptr.next
                prev.next = ptr
            else:
                prev, ptr = ptr, ptr.next
        return dummy.next
