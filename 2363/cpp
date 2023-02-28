class Solution {
public:
    vector<vector<int>> mergeSimilarItems(vector<vector<int>>& items1, vector<vector<int>>& items2) {
        vector<int> value_int(1000,0);
        vector<vector<int>> value_merge;
        for (int i=0; i<items1.size();++i){
            value_int[items1[i][0]-1] += items1[i][1]; 
        }
        for (int i=0; i<items2.size();++i){
            value_int[items2[i][0]-1] += items2[i][1];
        }
        for(int i=0; i<1000; ++i){
            if (value_int[i] != 0){
                value_merge.push_back(vector<int>{i+1, value_int[i]});
            }
        }
        return value_merge;
    }
};
