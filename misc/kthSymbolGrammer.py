class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(N,K):
            if(N==1 or K==1):
                return 0
            if(K==2):
                return 1
            curr = 2**(N-1)
            if(K>curr//2):
                ans = solve(N-1,K-curr//2)
                if ans==1:
                    return 0
                else:
                    return 1
            else:
                return solve(N-1,K)
        return solve(n,k)