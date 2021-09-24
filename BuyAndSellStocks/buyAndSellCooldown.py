class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        oldBuyStock = -1*prices[0]
        oldSellStock = 0
        oldCooldownStock = 0
        for i in range(1,len(prices)):
            newBuyStock=0
            newSellStock=0
            newCooldownStock=0
            if(oldCooldownStock-prices[i]>oldBuyStock):
                newBuyStock = oldCooldownStock-prices[i]
            else:
                newBuyStock = oldBuyStock
            if(oldBuyStock+prices[i]>oldSellStock):
                newSellStock = oldBuyStock+prices[i]
            else:
                newSellStock = oldSellStock
            if(oldSellStock>oldCooldownStock):
                newCooldownStock = oldSellStock
            else:
                newCooldownStock = oldCooldownStock
            oldBuyStock = newBuyStock
            oldSellStock = newSellStock
            oldCooldownStock = newCooldownStock
        return oldSellStock