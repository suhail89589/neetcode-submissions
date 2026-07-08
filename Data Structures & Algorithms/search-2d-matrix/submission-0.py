class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False


        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows*cols) - 1

        while l <= r:
            mid = l + (r - l) // 2

            row = mid // cols
            col = mid % cols

            element = matrix[row][col]

            if element == target:
                return True

            elif element < target:
                l = mid + 1

            else:
                r = mid - 1

        return False

        