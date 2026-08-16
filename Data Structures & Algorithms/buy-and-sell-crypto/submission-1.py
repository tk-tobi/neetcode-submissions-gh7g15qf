class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_purchase = prices[0]

        for i in range(1, len(prices)):
            min_purchase = min(prices[i], min_purchase)
            max_profit = max(max_profit, prices[i] - min_purchase)
        
        return max_profit



        