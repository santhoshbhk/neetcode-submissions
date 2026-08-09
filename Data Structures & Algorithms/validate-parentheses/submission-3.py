class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = ['(', '{', '[']
        closedBrackets = [')', '}', ']']

        stack = []

        if len(s) % 2 == 1:
            return False

        for ch in s:
            if ch in openBrackets:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top == '(' and ch != ')':
                    return False
                if top == '{' and ch != '}':
                    return False
                if top == '[' and ch != ']':
                    return False
        if len(stack) > 0:
            return False
        return True