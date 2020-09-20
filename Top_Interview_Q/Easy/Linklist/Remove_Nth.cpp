/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int listLen = 0;
        
        ListNode *root = head;
        while (root != NULL) {
            listLen++;
            root = root->next;
        }
        
        int i = listLen - n - 1;                
        if (i < 0) return head->next;
        
        root = head;
        
        int k = 0;
        while(k != i) {
            k++;
            root = root->next;            
        }
        
        root->next = root->next->next;
        return head;        
    }
};