class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = sorted(candidates)

        def backtrack(idx, curr, rem_target):
            if rem_target == 0:
                res.append(curr.copy())
                return 
            
            if rem_target < 0:
                return

            for i in range(idx, len(arr)):

                if i > idx and arr[i] == arr[i-1]:
                    continue
                
                if arr[i] > rem_target:
                    break
                curr.append(arr[i])
                backtrack(i + 1, curr, rem_target - arr[i])
                curr.pop()
                
        backtrack(0, [], target)
        return res

                

        