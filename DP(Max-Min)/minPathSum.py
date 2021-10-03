class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        t = [[float('inf') for i in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                temp = min(t[i-1][j],t[i][j-1])
                if(temp==float('inf')):
                    temp = 0
                t[i][j] = grid[i-1][j-1] + temp
        return t[m][n]
        
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m=len(grid)
    #     n=len(grid[0])
    #     t = {}
    #     def solve(top,left):
    #         key = (top,left)
    #         if(key in t):
    #             return t[key]
    #         if(top==0 and left==0):
    #             return 0
    #         op1 = float('inf')
    #         op2 = float('inf')
    #         if(top>=0):
    #             op1 = grid[top][left] + solve(top-1,left)
    #         if(left>=0):
    #             op2 = grid[top][left] + solve(top,left-1)
    #         t[key] = min(op1,op2)
    #         return t[key]
    #     return solve(m-1,n-1) + grid[0][0]