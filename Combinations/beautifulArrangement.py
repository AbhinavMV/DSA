class Solution:
    def countArrangement(self, n: int) -> int:
        
        perm = [i for i in range(1,n+1)]
        self.ans = 0
        def solve(arr,idx):
            if(len(arr)==0):
                self.ans+=1
                return
            for i,j in enumerate(arr):
                if(idx%j==0 or j%idx==0):
                    solve(arr[:i]+arr[i+1:],idx-1)
                       
        solve(perm,n)
        return self.ans