class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0

        char_num = {}
        max_length = 0

        for R in range(len(s)):
            char_num[s[R]] = 1 + char_num.get(s[R], 0)
            

            while (R-L+1)-max(char_num.values()) > k:
                char_num[s[L]] -= 1
                L += 1
            max_length = max(max_length, R-L+1)
            
        
        return max_length

            


            
        