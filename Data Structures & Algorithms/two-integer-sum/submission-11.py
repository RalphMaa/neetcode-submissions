class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} #Key is the num and value is the index

        for i in range(len(nums)):
            if i == 0:
                nums_map[nums[i]] = i
            else:
                diff = target - nums[i]
                # print("diff: ", diff)
                # print("nums_map", nums_map)
                if diff in nums_map:
                    return [nums_map[diff], i]
                else:
                    nums_map[nums[i]] = i
        

