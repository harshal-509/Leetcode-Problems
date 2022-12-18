class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n
        stack = []
        for i in range(n):
            while len(stack) and temp[i] > temp[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans
        