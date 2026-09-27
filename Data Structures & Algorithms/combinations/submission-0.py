class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def back(index, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return

            for i in range(index, n+1):
                curr.append(i)
                back(i+1, curr)
                curr.pop()

        back(1, [])
        return res
        