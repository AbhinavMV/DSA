class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        for i in range(1,len(prices)):
            if(prices[i]>=prices[i-1]):
                sell = i
            else:
                profit += prices[sell] - prices[buy]
                buy = sell = i
        profit += prices[sell] - prices[buy]
        return profit
        