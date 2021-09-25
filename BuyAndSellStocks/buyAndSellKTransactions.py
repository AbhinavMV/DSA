class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        size = len(prices)
        if k<1:
            return 0
        buy = [float('-inf')]*k
        sell = [0]*k
        for i in range(size):
            buy[0] = max(-prices[i],buy[0])
            sell[0] = max(buy[0]+prices[i],sell[0])
            for j in range(1,k):
                buy[j] = max(sell[j-1]-prices[i],buy[j])
                sell[j] = max(buy[j]+prices[i],sell[j])
        return sell[-1]
        