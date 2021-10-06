class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:    
        oldBuyStock = -1*prices[0]
        oldSellStock = 0
        for i in range(1,len(prices)):
            newBuyStock = 0
            newSellStock = 0
            if(oldSellStock-prices[i]>oldBuyStock):
                newBuyStock = oldSellStock - prices[i]
            else:
                newBuyStock = oldBuyStock
            if(oldBuyStock+prices[i]-fee>oldSellStock):
                newSellStock = oldBuyStock+prices[i]-fee
            else:
                newSellStock = oldSellStock
            oldBuyStock = newBuyStock
            oldSellStock = newSellStock
        return oldSellStock
            