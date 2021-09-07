class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        s = []

        for i in range(len(temperatures) - 1, -1, -1):
            while (len(s) != 0 and temperatures[s[-1]] <= temperatures[i]):
                s.pop()

            if len(s) == 0:
                res[i] = 0
            else:
                res[i] = s[-1] - i

            s.append(i)

        return res