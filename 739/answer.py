class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """   

        answer = [0 for i in range(len(temperatures))]
        helpStack = []

        for i in range(len(temperatures)):
            if len(helpStack) == 0:
                helpStack.append([i, temperatures[i]])
            else:
                while len(helpStack)!=0 and helpStack[-1][1]<temperatures[i]:
                    currentNode = helpStack[-1]
                    helpStack.pop()
                    answer[currentNode[0]] = i - currentNode[0]
                helpStack.append([i, temperatures[i]])
                
        return answer
