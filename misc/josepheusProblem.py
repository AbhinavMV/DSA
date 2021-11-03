class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        r = [i for i in range(1,n+1)]
        
        def solve(arr,idx,K):
            if(len(arr)==1):
                return arr[0]
            temp = (idx+k-1)%len(arr)
            return solve(arr[:temp]+arr[temp+1:],temp,K)
        
        return solve(r,0,k)