class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        waterCnt = 0
        leftHeight = [0 for i in range(len(height))]
        rightHeight = [0 for i in range(len(height))]

        for i in range(len(height)):
            if i==0:
                continue
            leftHeight[i] = max(height[i-1], leftHeight[i-1])
        
        for i in range(len(height)):
            if i==0:
                continue
            rightHeight[len(height)-i-1] = max(height[len(height)-i], rightHeight[len(height)-i])

        
        for i in range(len(height)):
            borderHeight = min(leftHeight[i], rightHeight[i])
            if borderHeight <= height[i]:
                continue
            waterCnt += (borderHeight - height[i])
        
        return waterCnt
