class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a,b : a + b,
            '-': lambda a,b : a - b,
            '*': lambda a,b : a * b,
            '/': lambda a,b : a / b,
        }
        for s in tokens:
            if s not in {"+", "-", "*", "/"}:
                stack.append(int(s))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(int(operations[s](a,b)))
        return stack[0]