class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                right = int(stack.pop())
                left = int(stack.pop())

                ans = 0

                if token == '+':
                    ans = left + right

                if token == '-':
                    ans = left - right
                
                if token == '*':
                    ans = left * right
                
                if token == '/':
                    ans = int(left / right)
                
                stack.append(str(ans))
        
        return int(stack[-1])