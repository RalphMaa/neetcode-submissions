class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        arr = [0] * 126
        max_length = 0

        for right in range(len(s)):
            arr[ord(s[right]) - ord("a")] += 1
            
            
            while left<right and arr[ord(s[right]) - ord("a")] > 1:
                arr[ord(s[left]) - ord("a")] -= 1
                left += 1
            
            max_length = max(max_length, right-left+1)
            
            # print("max_length: ", max_length)
            # print("arr: ", arr)
            # print("left: ", left)
            # print("right: ", right)
            # print()
        
        return max_length



        