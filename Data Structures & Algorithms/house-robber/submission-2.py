class Solution:
    def rob(self, nums: List[int]) -> int:
        
        index_money = [0] * len(nums)

        def recursive(house_money, curr_index):

            if curr_index >= len(nums):
                return 0
            
            if index_money[curr_index] > 0:
                return index_money[curr_index]
            
            max_money = nums[curr_index] + max(recursive(nums[curr_index], curr_index+2), recursive(nums[curr_index], curr_index+3))



            index_money[curr_index] = max_money

            return max_money
        
        if len(nums)>=2:
            money_1 = recursive(nums[0], 0)
            print()
            print(money_1)
            money_2 = recursive(nums[1], 1)
            print(money_2)
        elif len(nums)==1:
            return nums[0]



        return max(money_1, money_2)
            
            
            

        