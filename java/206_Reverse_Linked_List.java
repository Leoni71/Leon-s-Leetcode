# Iteration
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode new_head = null;
        while(head != null){
            ListNode temp = head.next;
            head.next = new_head;
            new_head = head;
            head = temp;
        }
        return new_head;
    }
}

# Recursion
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }
        ListNode p = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return p;
    }
}
