class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode ptr = head;
        while(ptr != null && ptr.next != null){
            if(ptr.next.val == ptr.val){
                ptr.next = ptr.next.next;
            }
            else{
                ptr = ptr.next;
            }
        }
        return head;
    }
}
