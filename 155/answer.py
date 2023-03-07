class MinStack(object):

    def __init__(self):
        self.valueVector = []
        self.minVector = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.valueVector.append(val)
        if len(self.minVector) == 0 or val < self.minVector[-1]:
            self.minVector.append(val)
        else:
            self.minVector.append(self.minVector[-1])



    def pop(self):
        """
        :rtype: None
        """
        self.valueVector.pop()
        self.minVector.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.valueVector[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minVector[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
