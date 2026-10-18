class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start, total):
            if total == target:          # complete answer: record and stop
                res.append(path[:])
                return
            if total > target:           # dead branch: stop
                return

            for i in range(start, len(nums)):   # choices: this index and rightward
                path.append(nums[i])
                backtrack(i, total + nums[i])   # i, not i+1: reuse is allowed
                path.pop()                      # undo

        backtrack(0, 0)
        return res