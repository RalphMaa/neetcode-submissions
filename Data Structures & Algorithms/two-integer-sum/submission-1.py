class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        index = 0
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in hashmap:
                return [hashmap[difference], i]
            else:
                hashmap[nums[i]] = i

            

        