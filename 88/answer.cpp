class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int index1 = 0, index2 = 0, arrayIndex = 0;
        vector<int> tmpNum;
        // vector<int>::iterator it = nums1.begin();
        while(index1 < m || index2 < n){
            if(index1 >= m){
                // nums1.insert(it, nums2[index2]);
                tmpNum.push_back(nums2[index2]);
                // it++;
                index2 += 1;
                arrayIndex += 1;
            }else{
                if (index2 >= n){

                    tmpNum.push_back(nums1[index1]);
                    index1 += 1;
                    // it++;
                    arrayIndex += 1;
                }else{
                    if (nums1[index1] < nums2[index2]){
                        tmpNum.push_back(nums1[index1]);
                        index1 += 1;
                        // it++;
                        arrayIndex += 1;
                    }else{
                        tmpNum.push_back(nums2[index2]);
                        // nums1.insert(it, nums2[index2]);
                        // it++;
                        index2 += 1;
                        arrayIndex += 1;
                    }
                }
            }
        }

        nums1 = tmpNum;
    }
};
