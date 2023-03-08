class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        currentPush = 0
        currentPop = 0
        while currentPush < len(pushed) or currentPop < len(popped):
            if currentPop == len(popped):
                return False
            if currentPush == len(pushed) and stack[-1] != popped[currentPop]:
                return False

            if len(stack) > 0 and stack[-1] == popped[currentPop]:
                currentPop += 1
                stack.pop()
            else:
                stack.append(pushed[currentPush])
                currentPush += 1
        
        return True
