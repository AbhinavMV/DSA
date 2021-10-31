class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def solve(N,K):
            if(N==1):
                return 0
            if(K==1):
                return 0
            curr = 2**(N)-1
            if(K==curr//2+1):
                return 1
            if(K>curr//2):   
                ans = solve(N-1,curr-K+1)
                if ans==1:
                    return 0
                else:
                    return 1
            else:
                return solve(N-1,K)
            
        return str(solve(n,k))
                