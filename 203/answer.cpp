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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *currentNode, *lastNode;
        currentNode = head;
        while (currentNode != NULL){
            if (currentNode == head){
                currentNode = currentNode ->next;
                lastNode = head;
            }else{
                if (currentNode -> val == val){
                    lastNode->next = currentNode ->next;
                    currentNode = lastNode->next;
                }else{
                    lastNode = currentNode;
                    currentNode = currentNode ->next;
                }
            }
        }

        if (!head){
            return NULL;
        }

        if (head->val == val){
            return head->next;
        }

        return head;

    }
};
