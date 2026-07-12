class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

       
        nums = nums1 + nums2
        nums.sort()
        
        
        n = len(nums)

        
        if n % 2 == 0:
            mid = n // 2
            mid_2 = mid - 1  
            med = (nums[mid] + nums[mid_2]) / 2
            return med

      
        elif n % 2 != 0:
            mid = n // 2  
            med = nums[mid]
            return float(med)
