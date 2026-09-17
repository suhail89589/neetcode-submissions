class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        add = nums[-1] * nums[-2]
        add_2 = nums[0] * nums[1]
        return abs(add - add_2)
        