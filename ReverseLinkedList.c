/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    if (head == NULL){
        return NULL;
    }
    else if (head->next == NULL){
        return head;
    }
    struct ListNode *current, *prev, *temp;
    current = head->next;
    prev = head;
    prev->next = NULL;
    temp = current->next;

    while(temp!=NULL){
        current->next = prev;
        prev = current;
        current = temp;
        temp = current->next; 
    }
    current->next = prev;
    
    return current;
}
