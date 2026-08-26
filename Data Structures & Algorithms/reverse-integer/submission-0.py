class Solution:
    def reverse(self, x: int) -> int:
        maximum = 2147483647 
        minimum = -2147483648
        

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > maximum // 10 or (res == maximum // 10 and digit > maximum % 10):
                return 0
            if res < minimum // 10 or ( res == minimum // 10 and digit < minimum % 10):
                return 0
            res = (res * 10) + digit

        return res

        
        