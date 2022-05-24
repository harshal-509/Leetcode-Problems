class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [(-1, ")")]
        answer = 0
        for i, c in enumerate(s):
            if c == ')' and stack[-1][1] == '(':
                stack.pop()
                answer = max(answer, i - stack[-1][0])
            else:
                stack.append((i, c))
        return answer