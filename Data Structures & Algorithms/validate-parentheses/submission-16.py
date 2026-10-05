class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {"}": "{", "]": "[", ")": "("}

        for a in s:
            if a in close_to_open:
                if stack and stack[-1] == close_to_open[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)

        return True if not stack else False