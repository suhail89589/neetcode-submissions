class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, curr_path, rem_target):
            if rem_target == 0:
                res.append(curr_path.copy())
                return
            
            if rem_target < 0:
                return

            for i in range(index,len(nums)):
                curr_path.append(nums[i])
                backtrack(i,curr_path, rem_target - nums[i] )
                curr_path.pop()



        backtrack(0, [], target)
        return res


        