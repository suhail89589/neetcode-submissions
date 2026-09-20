class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index: int, current_xor:int) -> int:
            if index == len(nums):
                return current_xor


            exclude_sum = backtrack(index+1, current_xor)
            include_sum = backtrack(index+1, current_xor ^ nums[index])

            return exclude_sum + include_sum

        return backtrack(0, 0)
        