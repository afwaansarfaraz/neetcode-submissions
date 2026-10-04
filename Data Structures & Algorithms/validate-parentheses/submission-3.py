class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:

            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)

            if ch in pairs:
                if not stack:
                    return False

                if stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False

        return not stack