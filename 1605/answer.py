class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(len(colSum))] for j in range(len(rowSum))]
        
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                result[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= result[i][j]
                colSum[j] -= result[i][j]

        return result
