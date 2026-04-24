'''
Understand:
we have a string with different brackets
every single opening bracket has to have its own closing bracket of the same type
they have to be closed in the same order

Input: s = "([{}])"
output = true


Plan:
for loop that pushes every opening bracket onto the stack
    {
    [
    (
    if we encounter a closing bracket, check at the top of the stack if there is its corresponding opening bracket
        if not: return false
        else: return true

'''



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in pairs:  # closing bracket
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:  # opening bracket
                stack.append(char)

        return len(stack) == 0





