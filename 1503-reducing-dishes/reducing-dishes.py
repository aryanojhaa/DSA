from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[0] * (n + 2) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for t in range(n, 0, -1):
                take = satisfaction[i] * t + dp[i + 1][t + 1]
                skip = dp[i + 1][t]
                dp[i][t] = max(take, skip)
        return dp[0][1]