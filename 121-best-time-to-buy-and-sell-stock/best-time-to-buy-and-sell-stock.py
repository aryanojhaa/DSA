class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = float('inf')
        max_profit = 0
        for i in prices:
            min_profit = min(min_profit,i)
            max_profit = max(max_profit,i-min_profit)
        return max_profit
        