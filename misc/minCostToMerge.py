class Solution:
#Time Limit Exceeded 
    def mergeStones(self, stones: List[int], k: int) -> int:
        ans = self.solve(stones,0,k)
        return ans if(ans!=float('inf')) else -1
    
    def solve(self,arr,curr,k):
        l = len(arr)
        out1 = 0
        out2 = 0
        if(l==1):
            return 0
        elif(l<k or l-curr<k):
            return float('inf')
        elif(l-curr>=k):
            out = sum(arr[curr:curr+k])
            out1 = out + self.solve(arr[:curr]+[out]+arr[curr+k:],0,k)
        out2 = self.solve(arr,curr+1,k)
        return min(out1,out2)