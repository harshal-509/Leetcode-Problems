class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        S = sum(nums)
        if S < x: 
            return -1
        ans = n+1
        seen = {}
        left = 0
        for i in range(n):
            left += nums[i]
            right = S-left
            mid = x-right
            if right == x:
                ans = min(ans, n-i-1)
            if left == x:
                ans = min(ans, i+1)
            if mid in seen:
                ans = min(ans, n-i+seen[mid])
            seen[left] = i
        return ans if ans < n+1 else -1