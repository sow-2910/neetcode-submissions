class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #add open parenthesis if open < n
        # only add a closing parenthesis if closed < open
        # valid if open == closed == n

        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))

            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res
            




