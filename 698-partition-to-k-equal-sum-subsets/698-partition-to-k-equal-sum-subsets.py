class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)
        if target % k != 0: return False
        target //= k
        cur = [0] * k
        nums.sort(reverse = True)
        def foo(index):
            if index == len(nums): 
                return True
            for i in range(k):
                if nums[index] + cur[i] <= target:
                    cur[i] += nums[index]
                    if foo( index + 1):
                        return True
                    cur[i] -= nums[index]
                if cur[i] == 0: 
                    break
            return False
        return foo(0)