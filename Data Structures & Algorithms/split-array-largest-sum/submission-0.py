class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left+right)//2
            curr_sum = 0
            subarray = 1

            for n in nums:
                
                if curr_sum + n > mid:
                    subarray += 1
                    curr_sum = n
                else:
                    curr_sum += n
            if subarray <= k:
                right = mid
            else:
                left = mid+1
        return left

        