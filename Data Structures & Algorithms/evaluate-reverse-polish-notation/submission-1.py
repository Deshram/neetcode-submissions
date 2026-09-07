class Solution:
    def operate(self, operand1, operand2, operator):
        operand1 = int(operand1)
        operand2 = int(operand2)

        if operator == "+":
            return str(operand1 + operand2)
        elif operator == "-":
            return str(operand1 - operand2)
        elif operator == "*":
            return str(operand1 * operand2)
        elif operator == "/":
            return str(int(operand1 / operand2)) 

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 3:
            return int(tokens[0])

        operations = ["+", "-", "*", "/" ]

        stack = []


        for token in tokens:
            if token in operations:
                opr1 = stack.pop()
                opr2 = stack.pop()
                stack.append(self.operate(opr2, opr1, token))
            else:
                stack.append(token)

        return int(stack[-1])