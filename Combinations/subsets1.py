class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def solve(arr,path):
            if(len(arr)<0):
                return
            results.append(path)
            for i in range(len(arr)):
                solve(arr[i+1:],path+[arr[i]])
            
        solve(nums,[])
        return results