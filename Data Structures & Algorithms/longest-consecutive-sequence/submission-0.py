class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Hashset = set(nums)
        longest = 0
        for n in Hashset:
            if (n-1) not in Hashset:
                length = 1

                while (n + length) in Hashset:
                    length += 1
                longest = max(longest,length)

        return longest

        