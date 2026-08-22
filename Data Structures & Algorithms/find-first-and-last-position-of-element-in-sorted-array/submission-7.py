class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first():
            l,r = 0, len(nums)

            while l < r:
                m = (l+r)//2

                if nums[m] < target:
                    l = m+1
                else:
                    r = m
            return l
        
        def last():
            l,r = 0, len(nums)

            while l < r:
                m = (l+r)//2
                if nums[m] <= target:
                    l = m+1
                else:
                    r = m
            return l-1
        f = first()
        l = last()

        if f < len(nums) and nums[f] == target:
            return [f,l]
        return [-1,-1]