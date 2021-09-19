class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        global t
        t = {}
        return self.solve(arr,0,len(arr)-1)
    
    def solve(self,arr,l,r):
        global t
        key = (l,r)
        if key in t:
            return t[key]
        if(l>=r):
            return 0
        ans = float('inf')
        for k in range(l,r):
            product = max(arr[l:k+1])*max(arr[k+1:r+1])
            temp = product + self.solve(arr,l,k)+self.solve(arr,k+1,r)
            ans = min(ans,temp)
        t[key] = ans
        return ans
        