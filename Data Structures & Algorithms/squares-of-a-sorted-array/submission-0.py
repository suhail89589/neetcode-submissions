class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = [x**2 for x in nums]
        squared_nums.sort()
        return squared_nums

        