class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode();
        ListNode prev = dummy, curr = head;
        prev.next = curr;
        
        while(curr!=null){
            if(curr.val == val){
                prev.next = curr.next;
                curr = curr.next;
            }
            else{
                prev = curr;
                curr = curr.next;
            }
        }
        return dummy.next;
        
    }
}
