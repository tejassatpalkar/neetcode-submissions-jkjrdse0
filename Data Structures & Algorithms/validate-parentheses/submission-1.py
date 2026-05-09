def isEndValid(stack, c):
        if len(stack) == 0:
            return False
        end = stack[-1]
        return end == '(' and c == ')' or \
            end == '{' and c == '}' or \
            end == '[' and c == ']'
def isOpen(p):
        return p == '(' or p == '[' or p ==  '{'

class Solution:

    
    
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if isOpen(p):
                stack.append(p)
            elif isEndValid(stack, p):
                stack.pop()
            else:
                return False
        return len(stack) == 0
            
        