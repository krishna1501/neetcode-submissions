class Solution:
    def calPoints(self, operations: List[str]) -> int:
        target = 0
        stack = []
        for i in operations:
            if i != "C" and i != "D" and i != "+":
                stack.append(int(i))
                print(stack)
                
            else:
                if i == "+":
                    stack.append(int(stack[-2]) + int(stack[-1]))
                    print(stack)
                if i  == "C":
                    print(stack)
                    stack.pop()
                    
                if i == "D":
                    stack.append(2 * int(stack[-1]))
                    print(stack)
        
        return sum(stack)
                