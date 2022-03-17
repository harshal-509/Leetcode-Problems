class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        i, count = 0, 0
        for c in s:
            count += 1 if c == '(' else -1
            i += 1
            if count == 0:
                break
        if i > 2:
            return 2 * self.scoreOfParentheses(s[1:i-1]) + self.scoreOfParentheses(s[i:]) 
        else:
            return 1 + self.scoreOfParentheses(s[i:])