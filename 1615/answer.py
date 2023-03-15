class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        roadsNum = [0 for i in range(n)]
        for i in range(len(roads)):
            roadsNum[roads[i][0]] += 1
            roadsNum[roads[i][1]] += 1
        
        resultMax = -1
        tmpMax = -1
        for i in range(n):
            for j in range(i+1, n):
                tmpMax = roadsNum[i] + roadsNum[j]
                if [i,j] in roads or [j,i] in roads:
                    tmpMax -= 1
                resultMax = max(resultMax, tmpMax)
        
        return resultMax
