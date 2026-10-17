class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums)+1)] 

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for j, m in count.items():
            arr[m].append(j)
        
        res = []
        for l in range(len(arr)-1, 0, -1):
            for num in arr[l]:
                res.append(num)
                if len(res) == k:
                    return res


