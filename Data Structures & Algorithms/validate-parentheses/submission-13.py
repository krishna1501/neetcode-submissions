class Solution:
    def isValid(self, s: str) -> bool:
        paramap ={"}":"{",")":"(","]":"["}
        stack = []
        
        for i in s:
            if i not in paramap:
                stack.append(i)
            else: 
                if not stack or paramap[i] != stack.pop():
                    return False
                
        return not stack