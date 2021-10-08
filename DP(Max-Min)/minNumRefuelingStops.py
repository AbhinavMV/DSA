class Solution:
    def minRefuelStops(self,target:int, startFuel:int,stations:List[List[int]]) -> int:
        size = len(stations)
        dp = [[0]*(size+1) for i in range(size+1)]
        for i in range(size+1):
            dp[i][0] = startFuel

        for i in range(1,size+1):
            for j in range(1,i+1):
                dp[i][j] = dp[i-1][j]
                if(dp[i-1][j-1]>=stations[i-1][0]):
                    dp[i][j] = max(dp[i][j],dp[i-1][j-1]+stations[i-1][1])

        for i in range(size+1):
            if dp[size][i]>=target:
                return i
        return -1
            

        
#     def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:       
#         size = len(stations)
#         dp = {}
#         def solve(prev,curr,s,t):
#             key = (curr,s)
#             if key in dp:
#                 return dp[key]
#             if(curr==size):
#                 if(s>=t):
#                     return 0
#                 return float('inf')
#             if(s<=0 and t>0):
#                 return float('inf')
            
#             disCovered = stations[curr][0]-prev
#             temps = s - (disCovered)
#             if(temps<0):
#                 return float('inf')
#             tempsRefuel = temps + stations[curr][1]
#             tempt = t - (disCovered)
            
#             op1 = 1+solve(stations[curr][0],curr+1,tempsRefuel,tempt)
#             op2 = solve(stations[curr][0],curr+1,temps,tempt)
#             dp[key] = min(op1,op2)
#             return dp[key]
#         res = solve(0,0,startFuel,target)
#         return res if res!= float('inf') else -1