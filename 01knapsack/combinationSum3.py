class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        arr = [1,2,3,4,5,6,7,8,9]
        def solve(tk,tn,size,path):
            if(tk==0 and tn==0):
                results.append(path[:])
            elif(tk<0 or tn<0 or size>=len(arr)):
                return
            else:
                if(arr[size]<=tn):
                    solve(tk-1,tn-arr[size],size+1,path+[arr[size]])
                solve(tk,tn,size+1,path)
        solve(k,n,0,[])
        return results