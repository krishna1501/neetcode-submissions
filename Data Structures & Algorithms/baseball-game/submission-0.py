class Solution:
    def calPoints(self, operations: List[str]) -> int:
        target = 0
        stack = []
        for i in operations:
            if i != "C" and i != "D" and i != "+":
                stack.append(i)
                print(stack)
                
            else:
                if i == "+":
                    stack.append(int(stack[-2]) + int(stack[-1]))
                    print(stack)
                if i  == "C":
                    print(stack)
                    stack.pop()
                    
                if i == "D":
                    stack.append(2*int(stack[-1]))
                    print(stack)
        while(len(stack)>0):
            target += int(stack.pop())
        return target
                