class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        box = []

        for  i in range(n-k, n):
            box.append(nums[i])


        result = box + nums[:n - k]

        nums[:] = result
        