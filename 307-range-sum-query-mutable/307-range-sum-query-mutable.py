class NumArray:

    def __init__(self, nums: List[int]):
        self.num_array=nums
        self.pre_sum=sum(self.num_array)
    def update(self, index: int, val: int) -> None:
        self.pre_sum=self.pre_sum - self.num_array[index] + val
        self.num_array[index]=val
    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum - sum(self.num_array[:left]) - sum(self.num_array[right+1:])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)