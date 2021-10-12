class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        t = {}
        
        def solve(r,c,maxMove):
            key = (r,c,maxMove)
            if key in t:
                return t[key]
            if(maxMove<0):
                return 0
            if(r<0 or r>=m or c< 0 or c>=n):
                return 1
            
            u = solve(r-1,c,maxMove-1) 
            v = solve(r+1,c,maxMove-1) 
            x = solve(r,c-1,maxMove-1) 
            y = solve(r,c+1,maxMove-1)
            t[key] = u+v+x+y
            return t[key]
        
        return solve(startRow,startColumn,maxMove) % 1000000007
        