'''
iterate through s
keep adding the opening brackets to the stack UNTIL we find a closing one
if we find one, we check the top of the stack to see if the the opening and closing brackets correspond to each other.
if they do, pop the opening bracket, continue
else,
return false

outside loop:
return true


'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "]":"[",
            ")":"(",
            "}":"{"
        }

        if len(s) % 2 != 0 or s[0] not in brackets.values():
            return False

        for c in s:
            if c in brackets.values():
                stack.append(c)
            elif stack and brackets[c] == stack.pop():
                continue
            else:
                return False
        
        return True if not stack else False
        
        