class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        path = []
        def backtrack(start: int):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
            
            return
        
        backtrack(0)
        return res