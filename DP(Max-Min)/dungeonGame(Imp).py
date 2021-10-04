class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        t = {}
        def solve(right,down):
            key = (right,down)
            if key in t:
                return t[key]
            if(right==n-1 and down==m-1):
                return max(1,-dungeon[down][right]+1)
            op1 = float('inf')
            op2 = float('inf')
            if(right+1<n):
                op1 = solve(right+1,down)
            if(down+1<m):
                op2 = solve(right,down+1)
            
            ans = min(op1,op2)            
            minHealth = ans+(-dungeon[down][right])
            t[key] = max(1,minHealth)
            return t[key]
                        
        return solve(0,0)