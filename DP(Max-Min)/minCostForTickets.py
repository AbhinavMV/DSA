class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        size = len(days)
        dp = [-1]*366  
        for i in days:
            dp[i] = 0          
        dp[0] = 0
        for i in range(1,366): 
            if(dp[i]!=-1):
                dp[i] = min(dp[i-1]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]
    
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         size = len(days)
#         t = {}
#         def solve(start):
#             if start in t:
#                 return t[start]
            
#             if(start>=size):
#                 return 0
            
#             costof1 = costs[0] + solve(start+1)
            
#             i=start
#             while(i<size and days[i]<(days[start]+7)):
#                 i+=1
#             costofweek = costs[1] + solve(i)
            
#             i=start
#             while(i<size and days[i]<(days[start]+30)):
#                 i+=1
#             costofmonth = costs[2] + solve(i)
            
#             t[start] = min(costof1,costofmonth,costofweek)
#             return t[start]
#         return solve(0)