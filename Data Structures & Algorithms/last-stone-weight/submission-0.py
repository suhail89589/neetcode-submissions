class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        elif len(stones) == 1:
            return stones[0]

        stones.sort()
        y = stones.pop()
        x = stones.pop()

        if x != y:
            stones.append(y-x)

        return self.lastStoneWeight(stones)

        