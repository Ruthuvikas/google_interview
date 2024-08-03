class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.bit = [0] * (self.n + 1)
        self.construct_bit(nums)

    def update_bit(self, index, val):
        index += 1
        while index <= self.n:
            self.bit[index] += val
            index += (index & -index)

    def construct_bit(self, nums):
        for i in range(self.n):
            self.update_bit(i, nums[i])

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.update_bit(index, diff)
    
    def get_sum(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= (index & -index)
        return res
    def sumRange(self, left: int, right: int) -> int:
        return self.get_sum(right) - self.get_sum(left - 1)

#Time Complexity
# construct_bit : O(nlogn)
# update_bit: O(logn)
# update: O(logn)
# get_sum: O(logn)
# sumRange: O(n)

#Space Complexity O(n)
