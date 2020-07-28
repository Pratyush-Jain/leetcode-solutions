class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        if len(prices) ==0:
            return 0
        price = max(prices)+1
        for i in range(len(prices)):
            if (prices[i]< price):
                price = prices[i]
            elif (prices[i]-price)> profit:
                profit = prices[i]-price
        return profit
                
        
