class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        prefix = 1
        for i in range (n):
            pre[i] = prefix
            prefix *= nums[i]
        

        suffix = 1
        for i in range(n -1, -1 , -1):
            pre[i] *= suffix
            suffix *= nums[i]

        return pre
            