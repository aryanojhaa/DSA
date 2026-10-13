from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        def solve(i, time):
            if i == n:
                return 0
            if dp[i][time] != -1:
                return dp[i][time]
            take = satisfaction[i] * time + solve(i + 1, time + 1)
            skip = solve(i + 1, time)
            dp[i][time] = max(take, skip)
            return dp[i][time]
        return solve(0, 1)
