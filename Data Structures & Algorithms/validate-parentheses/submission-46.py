class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {"}": "{", ")": "(", "]": "["}

        if len(s) == 0:
            return False
        elif s[0] in close_to_open:
            return False

        for i in s:
            if i in close_to_open:
                o = close_to_open.get(i)
                if stack and stack[-1] == o:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        if len(stack) == 0:
            return True
        
        return False
            