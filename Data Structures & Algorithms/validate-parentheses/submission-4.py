class Solution:
    def isValid(self, s: str) -> bool:
        new_stack = []
        pairs={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for char in s:
            if char not in pairs.keys():
                new_stack.append(char)
            elif char in pairs.keys() and len(new_stack) != 0:
                print(new_stack[-1],pairs[char])
                if new_stack[-1] == pairs[char]:
                    new_stack.pop()
                else:
                    return False
            else:
                return False
        if len(new_stack) == 0:
            return True
        else:
            return False