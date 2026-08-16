class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_purchase = float('inf')

        for price in prices:
            min_purchase = min(min_purchase, price)
            max_profit = max(price - min_purchase, max_profit)
        
        return max_profit



        