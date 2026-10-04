class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_clean = re.sub(r"[^a-zA-Z0-9]", "", s).lower()


        s_clean_reverse = s_clean[::-1]

        if s_clean == s_clean_reverse:
            return True
        return False