
// struct ListNode {
//      int val;
//      ListNode *next;
//      ListNode(int x) : val(x), next(NULL) {
         
//      }
//  };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode result(0);
        ListNode* next = &result;
        int j = 0, i = 0;
        while (l1 || l2 || j) {
            i = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + j;
            j = i / 10;
            next->next = new ListNode(i % 10);
            // if (i >= 10) {
            //     next->next = new ListNode(0 + j);
            //     j = 1;
            // }         
            // else {
            //     next->next = new ListNode(i + j);
            //     j = 0;
            // }
                         
            next = next->next;               
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return result.next;
    }
};
