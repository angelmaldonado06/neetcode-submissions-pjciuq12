import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens[0])

        stack = []
        valid_ari = {"+": operator.add,
                    "-": operator.sub, 
                    "*": operator.mul
                }

        for s in tokens:
            if s in valid_ari and len(stack) > 1:
                x = int(stack.pop())
                y = int(stack.pop())

                stack.append(valid_ari[s](y,x))
            elif s == "/":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(int(y/x))
            else:
                stack.append(s)

        return stack[-1]