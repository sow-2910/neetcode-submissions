class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s not in {"+", "-", "*", "/"}:
                stack.append(int(s))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if s == "+":
                    stack.append(num1 + num2)
                elif s == "-":
                    stack.append(num1 - num2)
                elif s == "*":
                    stack.append(num1 * num2)
                elif s == "/":
                    stack.append(int(num1 / num2))
        return stack[0]