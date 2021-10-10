class Solution:
    def uniquePaths(self,m:int,n:int) -> int:
        dp = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        
#     def uniquePaths(self, m: int, n: int) -> int:
#         t= {}
#         def solve(r,c):
#             key = (r,c)
#             if(key in t):
#                 return t[key]
#             if(r==0 or c==0):
#                 return 1
#             elif(r<0 or c<0):
#                 return 0
#             else:
#                 t[key] = solve(r-1,c)+solve(r,c-1)
#                 return t[key]
            
#         return solve(m-1,n-1)