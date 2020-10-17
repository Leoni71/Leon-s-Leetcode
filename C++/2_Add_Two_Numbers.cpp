/** 
* Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode *p = &dummy;
        int carry = 0;
        
        while(l1 || l2){
            int x = l1 ? l1->val : 0;
            int y = l2 ? l2->val : 0;
            int s = x+y+carry;
            carry = s/10;
            p->next = new ListNode(s%10);
            p = p->next;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        if(carry){
            p->next = new ListNode(carry);
        }
        return dummy.next;
    }
};
