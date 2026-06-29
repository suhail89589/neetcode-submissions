class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n-1):
            max_idx = i + 1


            for j in range(i+1, n):
                if arr[j] > arr[max_idx]:
                    max_idx = j


            arr[i] = arr[max_idx]
            
        if len(arr) > 0:
            arr[-1] = -1

        return arr

        

        