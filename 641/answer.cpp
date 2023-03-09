class MyNode{
public:
    int value;
    MyNode* next;

    MyNode(int Value, MyNode* Next=NULL){
        value = Value;
        next = Next;
    }
};


class MyCircularDeque {
private:
    int maxNum;
    int currentNum;
    MyNode *head=NULL, *tail=NULL;
    
public:
    MyCircularDeque(int k) {
        maxNum = k;
        currentNum = 0;
        if (head){
            delete head;
            head = NULL;
        }
        if (tail){
            delete tail;
            tail = NULL;
        }
    }
    
    bool insertFront(int value) {
        MyNode *tmpNode;
        if (currentNum == maxNum){
            return false;
        }

        if (currentNum==0){
            head = new MyNode(value);
            tail = head;
            currentNum += 1;
        }else{
            tmpNode = head;
            head = new MyNode(value, tmpNode);
            currentNum += 1;
        }

        return true;
    }
    
    bool insertLast(int value) {
        MyNode *tmpNode;
        if (currentNum == maxNum){
            return false;
        }

        if (currentNum==0){
            head = new MyNode(value);
            tail = head;
            currentNum += 1;
        }else{
            tmpNode = new MyNode(value);
            tail->next = tmpNode;
            tail = tail->next;
            currentNum += 1;
        }

        return true;

    }
    
    bool deleteFront() {
        MyNode *tmpNode;
        if (currentNum==0){
            return false;
        }else{
            if (currentNum==1){
                currentNum -= 1;
                delete head;
                head = NULL;
                tail = NULL;
            }else{
                tmpNode = head;
                head = head->next;
                delete tmpNode;
                currentNum -= 1;
            }
        }
        return true;
    }
    
    bool deleteLast() {
        MyNode *tmpNode;
        
        if (currentNum == 0){
            return false;
        }else{
            if (currentNum == 1){
                currentNum -= 1;
                delete head;
                head = NULL;
                tail = NULL;
            }else{
                tmpNode = head;
                while(tmpNode->next != tail){
                    tmpNode = tmpNode->next;
                }
                delete tail;
                tail = tmpNode;
                currentNum -= 1;
            }
        }
        return true;

    }
    
    int getFront() {
        if (currentNum == 0){
            return -1;
        }else{
            return head->value;
        }
    }
    
    int getRear() {
        if (currentNum == 0){
            return -1;
        }else{
            return tail->value;
        }

    }
    
    bool isEmpty() {
        return currentNum==0;
    }
    
    bool isFull() {
        return currentNum==maxNum;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */
