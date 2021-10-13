class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        #  to find total probability consider this each move prob is 1/8 or 0.125
        #  so for 0,0 there are two valid moves 1,2 & 2,1 prob is 1/8 + 1/8 
        #  then from 1,2 or 2,1 there are two valid moves so its prob will be 2/8
        #  then total prob will be 1/8*2/8 + 1/8*2/8 = 0.0625
        
        
        d = [[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2,],[2,-1],[2,1],[1,2]]
        t = {}
        
        def solve(N,K,r,c):
            key = (K,r,c)
            if key in t:
                return t[key]
            if(r<0 or r>=N or c<0 or c>=N):
                return 0
            if(K==0):
                return 1
            ans = 0
            for i in d:
                ans+= 0.125*solve(N,K-1,r+i[0],c+i[1])
            t[key] = ans
            return t[key]
            
        return solve(n,k,row,column)