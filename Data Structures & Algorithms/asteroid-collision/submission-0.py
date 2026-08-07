class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for element in asteroids:
            while stack and stack[-1] > 0 and element < 0:

                if stack[-1] > abs(element):
                    break

                elif stack[-1] == abs(element):
                    stack.pop()
                    break

                else:
                    stack.pop()
                    continue

            else:
                stack.append(element)

        return stack

        