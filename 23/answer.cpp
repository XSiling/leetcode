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
private:
    static bool cmp(ListNode *a, ListNode *b){
        if (b == NULL){
            return true;
        }else{
            if (a == NULL){
                return false;
            }else{
                return a->val < b->val;
            }
        }
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        

        if (lists.size() == 0){
            return NULL;
        }

        vector<ListNode*> countVector;
        ListNode *currentNode;
        ListNode *fakeStartNode;
        fakeStartNode = new ListNode(0);
        currentNode = fakeStartNode;
        int j = 0;
        for(int i=0;i<lists.size();++i){
            countVector.push_back(lists[i]);
        }
        sort(countVector.begin(), countVector.end(), cmp);
        while(countVector[0] != NULL){
            currentNode->next = countVector[0];
            currentNode = currentNode->next;
            countVector.erase(countVector.begin());
            if (currentNode->next == NULL){
                countVector.push_back(currentNode->next);
            }else{
                j = 0;
                while(j < countVector.size() && countVector[j] && countVector[j]->val < currentNode->next->val){
                    j++;
                }
                countVector.insert(countVector.begin() + j, currentNode->next);
            }
        }
        return fakeStartNode->next;
    }
};
