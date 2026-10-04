class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_nums = {}

        for i in range(len(nums)):
            curr_num = nums[i]

            num_to_find = target - curr_num

            if num_to_find in hash_nums:
                return [hash_nums.get(num_to_find), i]
            
            hash_nums[nums[i]] = i

        return False
