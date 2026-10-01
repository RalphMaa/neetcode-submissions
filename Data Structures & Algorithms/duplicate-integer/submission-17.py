class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_seen = {}
        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted)-1):
            if nums_sorted[i] not in already_seen:
                if nums_sorted[i]==nums_sorted[i+1]:
                    return True
            already_seen[i]=True
        return False

        