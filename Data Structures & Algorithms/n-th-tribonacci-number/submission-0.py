class Solution:
    def tribonacci(self, n: int) -> int:
        t_0 = 0
        t_1 = 1
        t_2 = 1

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        res = 0
        for i in range(0, n-2):
            res = t_0 + t_1 + t_2 # t_3

            # Update t_0, t_1, t_2
            t_0 = t_1
            t_1 = t_2
            t_2 = res
        
        return res


        