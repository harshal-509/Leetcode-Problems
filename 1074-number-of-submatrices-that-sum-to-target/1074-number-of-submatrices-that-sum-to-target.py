class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)

        n = len(matrix[0])

        count = 0

        for i in range(m):

            nums = [0] * n

            for j in range(i, m):

                for k in range(n):

                    nums[k] += matrix[j][k]


                count += self.subarraySum(nums, target)

        return count

    

    def subarraySum(self, nums: List[int], k: int) -> int:

        freq_map = {0: 1}

        result = 0

        curr_sum = 0 

        for i in range(len(nums)):

            curr_sum += nums[i]

            if curr_sum - k in freq_map:

                result+=freq_map[curr_sum - k]

            freq_map[curr_sum] = freq_map.get(curr_sum, 0) + 1

        return result