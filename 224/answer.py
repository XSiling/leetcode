class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        post = []
        cal_stack = []
        # first construct the post expression
        i = 0
        sign = 1
        lastLeft = True
        while i < len(s):
            currentChar = s[i]
            if currentChar == " ":
                i += 1
                continue
            if currentChar == "(":
                stack.append(currentChar)
                lastLeft = True
                i += 1
                continue
            if currentChar == ")":
                while stack[-1] != "(":
                    post.append(stack[-1])
                    stack.pop()
                stack.pop() # pop "("
                i += 1
                lastLeft = False
                continue
            if currentChar == "+":
                while len(stack) != 0 and stack[-1] != "(":
                    post.append(stack[-1])
                    stack.pop()
                stack.append(currentChar)
                i += 1
                lastLeft = False
                continue
            if currentChar == "-":
                if i == 0 or lastLeft:
                    post.append("0")
                while len(stack) != 0 and stack[-1] != "(":
                    post.append(stack[-1])
                    stack.pop()
                stack.append(currentChar)
                i += 1
                lastLeft = False
                continue
            if (ord(currentChar)-ord('0'))>=0 and (ord(currentChar)-ord('0'))<=9:
                thisString = ""
                while i < len(s) and (ord(s[i])-ord('0'))>=0 and (ord(s[i])-ord('0'))<=9:
                    thisString += s[i]
                    i += 1
                post.append(thisString)
                lastLeft = False
                continue
        
        while len(stack) != 0:
            post.append(stack[-1])
            stack.pop()

        for i in range(len(post)):
            if post[i] == "+":
                opt1 = cal_stack[-1]
                cal_stack.pop()
                opt2 = cal_stack[-1]
                cal_stack.pop()
                opt = int(opt1) + int(opt2)
                cal_stack.append(str(opt))
                continue
            if post[i] == "-":
                opt2 = cal_stack[-1]
                cal_stack.pop()
                if len(cal_stack) == 0:
                    opt1 = "0"
                else:
                    opt1 = cal_stack[-1]
                    cal_stack.pop()
                opt = int(opt1) - int(opt2)
                cal_stack.append(str(opt))
                continue
            cal_stack.append(post[i])

        return int(cal_stack[0])
            

        
