class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:    
        rows = len(matrix)
        columns = len(matrix[0])
        t = [[0 for i in range(columns+1)] for j in range(rows+1)]
        ans = float('-inf')
        for i in range(1,rows+1):
            for j in range(1,columns+1):
                if (matrix[i-1][j-1]=="1"):
                    t[i][j] = min(t[i-1][j],t[i][j-1],t[i-1][j-1]) +1 
                    ans = max(ans,t[i][j])
        return ans**2 if ans!=float('-inf') else 0
    
    
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
        
#         rows = len(matrix)
#         columns = len(matrix[0])
#         t = {}
        
#         def solve(r,c):
#             key = (r,c)
#             if key in t:
#                 return t[key]
            
#             if 0<=r<rows and 0<=c<columns:
#                 if matrix[r][c] == "1":
#                     t[key] = min(solve(r+1,c),solve(r,c+1),solve(r+1,c+1))+1
#                     return t[key]
#             t[key] = 0
#             return t[key]
        
#         ans = float('-inf')
#         for i in range(rows):
#             for j in range(columns):
#                 if matrix[i][j]=="1":
#                     temp = solve(i,j)
#                     ans = max(temp,ans)
#         return ans**2 if ans!=float('-inf') else 0
                