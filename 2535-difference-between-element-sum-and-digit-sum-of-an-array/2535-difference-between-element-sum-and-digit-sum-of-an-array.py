class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        a=0
        b=0
        for i in nums:
            a+=i
            b+=sum(list(map(int,str(i))))
        return abs(a-b)