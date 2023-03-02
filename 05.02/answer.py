class Solution(object):
    def printBin(self, num):
        """
        :type num: float
        :rtype: str
        """
        two_pow = [pow(2,i) for i in range(-1,-31,-1)]
        two_select = [0 for i in range(30)]
        last_index = -1
        result_str= "0."

        for i in range(30):
            if num >= two_pow[i]:
                num -= two_pow[i]
                two_select[i] = 1
                last_index = i

            
        if num != 0:
            return "ERROR"

        for i in range(last_index+1):
            if two_select[i] == 1:
                result_str += "1"
            else:
                result_str += "0"
        
        return result_str
