class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {
            "+": lambda a,b : a+b,
            # lambda Python me chhota anonymous function banata hai.
            "-": lambda a,b : a-b,
            "*": lambda a,b : a*b,
            "/": lambda a,b : int (a/b)
        }
        for token in tokens:
            if token not in operator:
                stack.append(int(token))
            else :
                right = stack.pop()
                left = stack.pop()
                result = operator[token](left , right)
                stack.append(result)        

        return stack[-1]