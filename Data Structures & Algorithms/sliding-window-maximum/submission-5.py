from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()      # holds INDICES; nums[dq[0]] >= nums[dq[1]] >= ... always
        result = []

        for i, x in enumerate(nums):
            # 1. Expire the front if its index has left the window [i-k+1, i]
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. Discard from the back anything <= x. Those elements are
            #    older than x AND no bigger, so they can never be a window max again.
            while dq and nums[dq[-1]] <= x:
                dq.pop()

            # 3. x is now a candidate; add it at the back
            dq.append(i)

            # 4. Once the first full window exists, the front is the max
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result