class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = {}
        for i in nums:
            nums_count[i] = 1 + nums_count.get(i, 0)

        # We now have the count for each character
        res = []
        for i in range(k): # Get the k most frequent numbers
            # Find max in HashMap
            max_key = max(nums_count, key = nums_count.get)

            # Add to res
            res.append(max_key)

            # Remove from Hashmap
            nums_count.pop(max_key, None)
        
        return res

            
