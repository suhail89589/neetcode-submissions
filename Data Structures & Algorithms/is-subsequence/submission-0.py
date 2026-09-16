class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        b = 0
        while len(s) > a and len(t) > b:
            if s[a] == t[b]:
                a += 1

            b += 1

        return len(s) == a