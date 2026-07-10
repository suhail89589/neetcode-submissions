class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
    
        for price in prices:
        # Update the lowest purchase price found so far
            if price < min_price:
                min_price = price
        # Check if selling today beats our best profit so far
            elif price - min_price > max_profit:
                max_profit = price - min_price
            
        return max_profit


        