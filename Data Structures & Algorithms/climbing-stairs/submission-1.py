class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        vec = [0] * (n + 1)

        vec[1] = 1
        vec[2] = 2

        for i in range(3, n+1):
            vec[i] = vec[i-1]
            vec[i] += vec[i-2]

        return vec[n]