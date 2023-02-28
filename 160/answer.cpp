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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *currentNode, *lastANode, *currentNode_B;
        bool find = false;
        int stepA = 0, stepB = 0, stepC = 0;
        currentNode = headA;
        while(currentNode->next != NULL){
            currentNode = currentNode->next;
            stepA += 1;
        }
        lastANode = currentNode;
        currentNode->next = headA;
        currentNode = headB;
        while(currentNode->next != NULL){

            if (currentNode == lastANode){
                find = true;
                break;
            }
            currentNode = currentNode->next;
            stepB += 1;
        }

        if (!find){
            lastANode->next = NULL;
            return NULL;

        }
        currentNode_B = headB;
        currentNode = headA;

        if ((stepA-stepB)>=0){
            for(int i=0;i<(stepA-stepB);++i){
                currentNode = currentNode->next;
            }
        }
        else{
            for(int i=0;i<(stepB-stepA);++i){
                currentNode_B = currentNode_B->next;
            }
        }

        while(currentNode != currentNode_B){
            currentNode = currentNode->next;
            currentNode_B = currentNode_B->next;
        }

        lastANode->next = NULL;
        return currentNode;


    }
};
