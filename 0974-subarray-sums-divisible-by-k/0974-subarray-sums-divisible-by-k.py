class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainderFrq = defaultdict(int)
        remainderFrq[0] = 1
        res = prefixSum = 0
        for n in nums:
            prefixSum += n
            remainder = prefixSum % k
            res += remainderFrq[remainder]
            remainderFrq[remainder] += 1
        return res