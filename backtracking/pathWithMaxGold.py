class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        results = []
        def solve(r,c,path):
            if(r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0):
                results.append(path)
                return
            
            for i,j in ([-1,0],[1,0],[0,1],[0,-1]):
                temp = grid[r][c]
                grid[r][c] = 0
                solve(r+i,c+j,path+temp)
                grid[r][c] = temp
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]!=0):
                    solve(i,j,0)
                    
        if(results==[]):
            return 0
        return max(results)