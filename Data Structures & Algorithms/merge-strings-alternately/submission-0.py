class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        box = []
        ptr_1 = 0
        ptr_2 = 0
        while ptr_1 < len(word1) or ptr_2 < len(word2):
            if ptr_1 < len(word1):
                box.append(word1[ptr_1])
                ptr_1 += 1
            if ptr_2 < len(word2):
                box.append(word2[ptr_2])
                ptr_2 += 1


        return "".join(box)
        