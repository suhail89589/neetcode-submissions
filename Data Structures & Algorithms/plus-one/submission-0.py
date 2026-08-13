class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(str(i) for i in digits))
        number = number + 1
        res = [int(digit) for digit in str(number)] 
        return res
 
