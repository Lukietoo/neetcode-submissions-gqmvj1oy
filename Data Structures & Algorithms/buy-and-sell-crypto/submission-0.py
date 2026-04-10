class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        current_max = 0
        
        while r < len(prices): 
            if prices[r] > prices[l]:
                current_profit = prices[r] - prices[l]
                current_max = max(current_max, current_profit)
            else:
                l = r
            
            r += 1
        
        return current_max