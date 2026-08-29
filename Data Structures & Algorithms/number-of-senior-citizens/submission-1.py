class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for s in details:
            cut = s[-4:]
            t = cut[:2]
            if int(t) > 60:
                count += 1
        return count





        