class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {"}": "{", ")": "(", "]": "["}

        if len(s) == 0:
            return False
        elif s[0] in close_to_open:
            return False

        for i in s:
            if len(stack) == 0 and i not in close_to_open:
                stack.append(i)
            elif i in close_to_open:
                open = close_to_open.get(i, 0)
                if len(stack) == 0:
                    return False
                elif stack[-1] == open:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(i)
    
        if len(stack) == 0:
            return True
        
        return False
            