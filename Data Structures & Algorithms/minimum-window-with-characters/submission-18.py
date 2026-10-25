class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        chars_t = {}
        for c in t:
            chars_t[c] = 1 + chars_t.get(c, 0)

        window = {}
        have, need = 0, len(chars_t)
        best_len = float("inf")
        best = (0, 0)

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if window[c]==chars_t.get(c, 0):              # c matters to t, and its count just reached what t needs
                have += 1

            while have == need:           # window is valid
                if (r - l + 1) < best_len:
                    best_len = r - l + 1
                    best = (l, r)
                left_c = s[l]
                window[left_c] -= 1
                if window[left_c]<chars_t.get(left_c, 0):          # left_c matters to t, and its count just dropped below what t needs
                    have -= 1
                l += 1

        return s[best[0]:best[1] + 1] if best_len != float("inf") else ""
