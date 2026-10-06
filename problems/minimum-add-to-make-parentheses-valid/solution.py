class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        min_moves = 0
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    min_moves += 1
        return min_moves + len(stack)