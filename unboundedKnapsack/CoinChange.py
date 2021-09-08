class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        size = len(coins)
        t = [[-1 for i in range(amount+1)] for i in range(size+1)]
        for i in range(size+1):
            for j in range(amount+1):
                if(i==0 and j>0):
                    t[i][j] = float('inf')
                elif(j==0):
                    t[i][j] = 0  
                elif(coins[i-1]<=j):
                    t[i][j] = min(1+t[i][j-coins[i-1]],t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        temp = t[size][amount]
        return -1 if temp == float('inf') else temp

#       memoised
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         global t
#         t = {}
#         temp = self.solve(coins,len(coins),amount)
#         return -1 if temp==float('inf') else temp
    
#     @classmethod
#     def solve(self,coins,size,amount):
#         global t
#         key = (size,amount)
#         if(key in t):
#             return t[key]
#         if(size==0 and amount>0):
#             return float('inf')
#         if(amount==0):
#             return 0
#         if(coins[size-1]<=amount):
#             t[key] = min(1+self.solve(coins,size,amount-coins[size-1]),self.solve(coins,size-1,amount))
#             return t[key]
#         t[key] = self.solve(coins,size-1,amount)
#         return t[key]