class Solution:
    def isValid(self, s: str) -> bool:
        paramap ={"}":"{",")":"(","]":"["}
        stack = []
        
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