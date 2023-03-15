class Solution {
public:
    void sortColors(vector<int>& nums) {
        //写个快排
        QuickSort(nums, 0, nums.size()-1);
    }

    void QuickSort(vector<int>& nums, int start, int end){
        int referValue;
        int i = start, j = end, tmp;
        if (start >= end){
            return;
        }
        referValue = nums[start];
        while (i<j){
            while(nums[j]>=referValue && i<j){
                j--;
            }
            while(nums[i]<=referValue && i<j){
                i++;
            }
            tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
        nums[start] = nums[j];
        nums[j] = referValue;

        QuickSort(nums, start, j-1);
        QuickSort(nums, j+1, end);
    }
};
