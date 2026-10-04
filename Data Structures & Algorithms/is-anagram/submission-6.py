class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
               
        a = list(s)
        b = list(t)

        if len(a) != len(b):
            return False
        
        count_S = {}
        count_T = {}

        for i in range(len(a)):
            count_S[a[i]] = count_S.get(a[i], 0) + 1
            count_T[b[i]] = count_T.get(b[i], 0) + 1
        return count_S == count_T

        
                

