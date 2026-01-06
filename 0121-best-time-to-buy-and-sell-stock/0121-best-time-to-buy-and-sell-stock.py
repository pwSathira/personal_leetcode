class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in prices[1:]:
            if buy_price > i:
                buy_price = i
            
            profit = max(profit, i - buy_price)
        
        return profit