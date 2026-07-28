class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        s = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while s and t > s[-1][1]:
                popped = s.pop()
                res[popped[0]] = i - popped[0]

            s.append((i, t))

        return res

