class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        minWhite = 101
        currentWhite = 0
        for i in range(k):
            if blocks[i] == 'W':
                currentWhite += 1
        minWhite = min(minWhite, currentWhite)
        
        for i in range(len(blocks)-k):
            if blocks[i] == 'W':
                currentWhite -= 1
            if blocks[k+i] == 'W':
                currentWhite += 1
            minWhite = min(minWhite, currentWhite)
        
        return minWhite

