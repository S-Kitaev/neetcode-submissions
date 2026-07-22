class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        if len(tokens) == 1:
            return int(tokens[0])

        result = 0
        pointer = 0

        while pointer < len(tokens):
            if tokens[pointer].isdigit() or tokens[pointer][1:].isdigit():
                stack.append(int(tokens[pointer]))
            elif tokens[pointer] in ['+', '-', '*', '/']:
                operation = 0
                if tokens[pointer] == '+':
                    operation = stack[-2] + stack[-1]
                elif tokens[pointer] == '-':
                    operation = stack[-2] - stack[-1]
                elif tokens[pointer] == '*':
                    operation = stack[-2] * stack[-1]
                elif tokens[pointer] == '/':
                    operation = stack[-2] / stack[-1]
                
                operation
                stack = stack[:-2] + [int(operation)]
            print(stack)
            pointer += 1

        return int(operation)


