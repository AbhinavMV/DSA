class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def solve(arr,n,t,res,results):
            if(t<=0 or n<0):
                if(t==0):
                    results.append(res)
                return
            if(arr[n]<=t):
                solve(arr,n,t-arr[n],res+[arr[n]],results)
            solve(arr,n-1,t,res,results)
            
        results = []
        solve(candidates,len(candidates)-1,target,[],results)
        return results