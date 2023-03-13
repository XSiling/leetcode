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
    ListNode* oddEvenList(ListNode* head) {
        ListNode *OddNode, *EvenNode, *OddStartNode, *EvenStartNode, *tmpNode1, *tmpNode2;

        if (head == NULL){
            return NULL;
        }

        if (head->next == NULL || head->next->next == NULL ){
            return head;
        }

        OddNode = head;
        EvenNode = head->next;
        OddStartNode = OddNode;
        EvenStartNode = EvenNode;

        while (1){
            if (EvenNode == NULL){
                break;
            }
            OddNode->next = EvenNode->next;
            if (OddNode->next == NULL){
                break;
            }else{
                OddNode = OddNode->next;
                EvenNode->next = OddNode->next;
                EvenNode = EvenNode->next;
            }
        }

        OddNode->next = EvenStartNode;

        return OddStartNode;





    }
};
