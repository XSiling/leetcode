class Solution(object):
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """
        currentWaitingCustomer = 0
        getMoney = []
        for i in range(len(customers)):
            currentWaitingCustomer += customers[i]
            if len(getMoney)==0:
                if currentWaitingCustomer >= 4:
                    currentWaitingCustomer -= 4
                    getMoney.append(boardingCost * 4 - runningCost)
                else:
                    getMoney.append(boardingCost * currentWaitingCustomer - runningCost)
                    currentWaitingCustomer = 0
            else:
                if currentWaitingCustomer >= 4:
                    currentWaitingCustomer -= 4
                    getMoney.append(getMoney[-1] + boardingCost * 4 - runningCost)
                else:
                    getMoney.append(getMoney[-1] + boardingCost * currentWaitingCustomer - runningCost)
                    currentWaitingCustomer = 0
        
        while (currentWaitingCustomer > 0):
            if currentWaitingCustomer >= 4:
                getMoney.append(getMoney[-1] + boardingCost * 4 - runningCost)
                currentWaitingCustomer -= 4
            else:
                getMoney.append(getMoney[-1] + boardingCost * currentWaitingCustomer - runningCost)
                currentWaitingCustomer = 0

        if max(getMoney) > 0:
            return getMoney.index(max(getMoney))+1
        else:
            return -1
