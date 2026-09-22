class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if price > prices[i]:
                price = prices[i]
            profit = max(profit, prices[i] - price)
        return profit