class Solution:
    def minCostClimbingStairs(self,cost:List[int])-> int:
        size = len(cost)
        dp = [0]*(size+1)
        dp[1] = cost[0]

        for i in range(2,size+1):
            dp[i] = cost[i-1] + min(dp[i-1],dp[i-2])
        return min(dp[size-1:size+1])
    
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         size = len(cost)
#         cost = [0]+cost
#         t = {}
        
#         def solve(curr):
#             if curr in t:
#                 return t[curr]
            
#             if(curr>size):
#                 return 0
            
#             op1 = cost[curr] + solve(curr+1)
#             op2 = cost[curr] + solve(curr+2)
            
#             t[curr] = min(op1,op2)
#             return t[curr]
        
#         return solve(0)