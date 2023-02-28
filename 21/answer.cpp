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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *currentNode_1, *currentNode_2, *resultNodeList=NULL, *resultNodeStart;
        currentNode_1 = list1;
        currentNode_2 = list2;

        while(currentNode_1 != NULL || currentNode_2 != NULL){
            if (currentNode_1 == NULL){
                if (resultNodeList == NULL){
                    resultNodeList = currentNode_2;
                    resultNodeStart = resultNodeList;
                    currentNode_2 = currentNode_2->next;
                }else{
                    resultNodeList->next = currentNode_2;
                    resultNodeList = resultNodeList->next;
                    currentNode_2 = currentNode_2->next;
                }
            }
            else{
                if (currentNode_2 == NULL){
                    if (resultNodeList == NULL){
                        resultNodeList = currentNode_1;
                        resultNodeStart = resultNodeList;
                        currentNode_1 = currentNode_1->next;
                    }else{
                        resultNodeList->next = currentNode_1;
                        resultNodeList = resultNodeList->next;
                        currentNode_1 = currentNode_1->next;
                    }

                }
                else{
                    if(currentNode_1->val > currentNode_2->val){
                        if (resultNodeList == NULL){
                            resultNodeList = currentNode_2;
                            resultNodeStart = resultNodeList;
                            currentNode_2 = currentNode_2->next;
                        }else{
                            resultNodeList->next = currentNode_2;
                            resultNodeList = resultNodeList->next;
                            currentNode_2 = currentNode_2->next;
                        }
                    }else{
                        if (resultNodeList == NULL){
                            resultNodeList = currentNode_1;
                            resultNodeStart = resultNodeList;
                            currentNode_1 = currentNode_1->next;
                        }else{
                            resultNodeList->next = currentNode_1;
                            resultNodeList = resultNodeList->next;
                            currentNode_1 = currentNode_1->next;
                        }

                    }

                }
            }
        }
        return resultNodeStart;
    }
};
