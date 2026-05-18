class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:
            print(stack)
            if t != "*" and t != "/" and t != "-" and t != "+":
                stack.append(int(t))
                continue
            b = stack.pop()
            a = stack.pop()
            result= 0
            if t == "+":
                result = a  + b
            elif t == "-":
                result = a -b
            elif t == "*":
                result = a * b 
            elif t == "/":
                result = int(a/b)
            
            stack.append(result)
            
            
        return stack[0]
        