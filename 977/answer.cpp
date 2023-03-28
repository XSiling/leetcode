class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int belowStart, aboveStart;
        vector<int> ans = {};
        if (nums[0] >= 0){
            for (int i=0; i<nums.size(); ++i){
                ans.push_back(nums[i] * nums[i]);
            }
            return ans;
        }

        if (nums[nums.size()-1] <= 0){
            for (int i=nums.size()-1; i>=0; --i){
                ans.push_back(nums[i] * nums[i]);
            }
            return ans;
        }

        for(int i=0; i<nums.size()-1; ++i){
            if (nums[i] < 0 && nums[i+1] >=0 ){
                belowStart = i;
                aboveStart = i + 1;
                break;
            }
        }

        while (belowStart >= 0 || aboveStart < nums.size()){
            if (belowStart < 0){
                ans.push_back(nums[aboveStart] * nums[aboveStart]);
                aboveStart++;
                continue;
            }
            if (aboveStart >= nums.size()){
                ans.push_back(nums[belowStart] * nums[belowStart]);
                belowStart--;
                continue;
            }
            if (abs(nums[belowStart]) < abs(nums[aboveStart])){
                ans.push_back(nums[belowStart] * nums[belowStart]);
                belowStart--;
            }else{
                ans.push_back(nums[aboveStart] * nums[aboveStart]);
                aboveStart++;
            }
        }

        return ans;


    }
};
