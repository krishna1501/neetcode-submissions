class Solution:
    def isValid(self, s: str) -> bool:
        paramap ={"}":"{",")":"(","]":"["}
        stack = []
        if len(s) % 2 != 0: 
            return False
        print(len(s) % 2)
        
        for i in s:
            if i not in paramap:
                stack.append(i)
            
            else: 
                if not stack:
                    return False
                if(paramap[i] == stack.pop()):
                    continue
                else:
                    return False
        return len(stack) == 0