# 首先排序
# 以每一个数字为中间基准，设置两边的指针，双指针依次向外寻找答案

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_list = []
        nums.sort()
        for i in range(1, len(nums)-1):
            leftAnchor = i - 1
            rightAnchor = i + 1
            while(leftAnchor >= 0 and rightAnchor < len(nums)):
                if (nums[i] + nums[leftAnchor] + nums[rightAnchor]):
                    
                    # not zero
                    if (nums[i] + nums[leftAnchor] + nums[rightAnchor]) < 0:
                        rightAnchor += 1
                        continue
                    if (nums[i] + nums[leftAnchor] + nums[rightAnchor]) > 0:
                        leftAnchor -= 1
                        continue
                else:
                    # sum equals to zero
                    if [nums[leftAnchor], nums[i], nums[rightAnchor]] not in result_list:
                        result_list.append([nums[leftAnchor], nums[i], nums[rightAnchor]])
                    leftAnchor -= 1
                    rightAnchor += 1
                
        
        return result_list
