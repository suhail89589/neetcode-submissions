class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left , right = 0, len(nums) - 1

        while left < right:
            if nums[left] == nums[left + 1]:
                return True
            
            if nums[right] == nums[right-1]:
                return True

            left += 1
            right -= 1

            
        return False