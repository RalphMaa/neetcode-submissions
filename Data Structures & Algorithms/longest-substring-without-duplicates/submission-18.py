class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_num = {}
        left = 0
        max_length = 0
        curr_length = 0
        for right in range(len(s)):
            char_num[s[right]] = 1 + char_num.get(s[right], 0)
            curr_length += 1

            while char_num[s[right]] > 1:
                char_num[s[left]] = char_num.get(s[left], 0) -1
                left += 1
                curr_length -= 1
            
            max_length = max(curr_length, max_length)
        
        return max_length
