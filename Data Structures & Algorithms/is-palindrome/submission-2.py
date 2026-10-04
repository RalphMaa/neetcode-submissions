class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_clean = re.sub(r"[^a-zA-Z0-9]", "", s).lower()

        i, j = 0, len(s_clean)-1

        while i<j:
            if s_clean[i]!=s_clean[j]:
                return False
            i = i+1
            j = j-1
        return True
        

