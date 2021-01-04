# Because it's sorted list, so just go straight forward
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head
