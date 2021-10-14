class Solution:
    def numTilings(self, n: int) -> int:
        t={}
        
        def solve(x,state):
            key = (x,state)
            if key in t:
                return t[key]
            if(x<=0):
                if(x==0 and state==0):
                    return 1
                return 0
            if(state==0):
                topBottomFree1 = solve(x-1,0)
                topBottomFree2 = solve(x-2,0)
                bottomFreeTromino = solve(x-1,1)
                topFreeTromino = solve(x-1,2)
                t[key] = (topBottomFree1 + topBottomFree2 + bottomFreeTromino + topFreeTromino) % (10**9 + 7)
                return t[key]
            elif(state==1):
                horizontalDominoBottom = solve(x-1,2)
                bottomFillTromino = solve(x-2,0)
                t[key] = (horizontalDominoBottom + bottomFillTromino) % (10**9 + 7)
                return t[key]
            elif(state==2):
                horizontalDominoTop = solve(x-1,1)
                topFillTromino = solve(x-2,0)
                t[key] = (horizontalDominoTop + topFillTromino) % (10**9 + 7)
                return t[key]
            
        return solve(n,0)
 
