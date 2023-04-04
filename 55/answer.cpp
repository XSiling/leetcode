/* reverse from the end */
/* like DP */

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int perStep = -1;
        vector<bool> canReach(nums.size(), false);
        canReach[nums.size()-1] = true;
        for(int i=nums.size()-2; i>=0; --i){
            perStep = nums[i];
            for (int j=0; j<=perStep; ++j){
                if ((i+j)>=nums.size()){
                    break;
                }
                if (canReach[i+j]==true){
                    canReach[i] = true;
                    break;
                }
            }
        }

        return canReach[0];
    }
};
