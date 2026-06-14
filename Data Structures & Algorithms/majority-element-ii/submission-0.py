from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        limit = n / 3

        freq = Counter(nums)

        res = []

        for number, count in freq.items():
            if count > limit:
                res.append(number)
        return res
        