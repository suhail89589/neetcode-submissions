class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        local_min = float("inf")
        minima = local_min
        while low <= high:
            mid = ( low + high) // 2
            if nums[low] <= nums[mid]:
                local_min = nums[low]
                low = mid +1
            else:
                local_min = nums[mid]
                high = mid - 1
            minima = min(minima, local_min)

        return minima
            
        
        
        