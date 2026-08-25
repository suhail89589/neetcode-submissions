class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            curr_ascii = ord(s[i])
            next_ascii = ord(s[i+1])

            res += abs(curr_ascii - next_ascii)

        return res
        