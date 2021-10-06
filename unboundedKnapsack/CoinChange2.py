class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        size = len(coins)
        t = [[-1 for i in range(amount+1)] for i in range(size+1)]
        for i in range(size+1):
            for j in range(amount+1):
                if(i==0 and j>0):
                    t[i][j] = 0
                elif(j==0):
                    t[i][j] = 1  
                elif(coins[i-1]<=j):
                    t[i][j] = t[i][j-coins[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[size][amount]
        
    # return self.solve(coins,len(coins),amount)
    
    # @classmethod
    # def solve(self,coins,size,amount):
    #     if(size==0 and amount>0):
    #         return 0
    #     if(amount==0):
    #         return 1
    #     if(coins[size-1]<=amount):
    #         return self.solve(coins,size,amount-coins[size-1])+self.solve(coins,size-1,amount)
    #     return self.solve(coins,size-1,amount)