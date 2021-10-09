class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:       
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[float('inf')]*(cols+2) for i in range(rows+1)]
        dp[1] = [float('inf')] + matrix[0] + [float('inf')]
        for i in range(2,rows+1):
            for j in range(1,cols+1):
                dp[i][j] = matrix[i-1][j-1] + min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        return min(dp[-1])
        
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
#         rows = len(matrix)
#         cols = len(matrix[0])
#         t = {}
#         def solve(r,c):
#             key = (r,c)
#             if key in t:
#                 return t[key]
#             if(r==rows):
#                 return 0
#             ans = float('inf')
#             op1 = float('inf')
#             if(c-1>=0):
#                 op1 = min(op1,solve(r+1,c-1))
#             op2 = float('inf')
#             if(c+1<cols):
#                 op2 = min(op2,solve(r+1,c+1))
#             ans = matrix[r][c] + min(op1,solve(r+1,c),op2)
#             t[key] = ans
#             return t[key]
#         ans = float('inf')
#         for i in range(cols):
#             ans = min(ans,solve(0,i))
            
#         return ans
        