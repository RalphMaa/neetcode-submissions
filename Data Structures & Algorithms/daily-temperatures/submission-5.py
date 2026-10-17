class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Index of temperatures = day
        # Value of temperatures = temp
        # Goal: For each day find the number of days until a warmer temperature appears, if no future warmer day -> Return 0

        # Method to solve: Use stack


        
        res = [0] * len(temperatures)
        stack = []

        for day in range(len(temperatures)):
                
            while stack and temperatures[day] > stack[-1][0]:
                num_days = day - stack[-1][1]
                res[stack[-1][1]] = num_days
                stack.pop()

            stack.append([temperatures[day], day])

        return res

                
            

        
        return res