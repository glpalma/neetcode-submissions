class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        s = []
        operators = {'+', '-', '*', '/'}

        for op in tokens:
            if op.isdigit() or (op[0] == '-' and op[1:].isdigit()):
                s.append(int(op))
            elif op in operators:
                op2 = int(s.pop())
                op1 = int(s.pop())

                if op == '+':
                    res = op1 + op2
                elif op == '-':
                    res = op1 - op2
                elif op == '*':
                    res = op1 * op2
                elif op == '/':
                    res = op1 / op2
                
                s.append(res)
            
        return int(s[-1])