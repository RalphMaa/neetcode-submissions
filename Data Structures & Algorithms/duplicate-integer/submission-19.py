class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        no_dup_length = len(set(nums))
        if no_dup_length == length:
            return False
        return True