class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = float('inf')
        profitTemp = 0
        op = 0
        for i in range(len(prices)):
            if(least>prices[i]):
                least = prices[i]
            profitTemp = prices[i] - least
            if(profitTemp>op):
                op = profitTemp
        return op
        
        #Brute Force
        # size  = len(prices)
        # ans = 0
        # for i in range(size):
        #     for j in range(i,size):
        #         temp = prices[j]-prices[i]
        #         if(temp>0 and temp>ans):
        #             ans = temp
        # return ans
        