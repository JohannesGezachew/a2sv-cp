class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operations:
                x = stack.pop()
                y = stack.pop()
                if token == "+":
                    stack.append(y + x)
                elif token == "-":
                    stack.append(y - x)
                elif token == "*":
                    stack.append(y * x)
                elif token == "/":
                    stack.append(int(y / x))
            else:
                stack.append(int(token))

        return stack[-1]