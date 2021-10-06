class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstBuy = float('-inf')
        firstSell = 0
        secondBuy = float('-inf')
        secondSell = 0
        
        for i in range(len(prices)):
            firstBuy = max(-prices[i],firstBuy)
            firstSell = max(firstBuy+prices[i],firstSell)
            secondBuy = max(firstSell-prices[i],secondBuy)
            secondSell = max(secondBuy+prices[i],secondSell)
            
        return secondSell