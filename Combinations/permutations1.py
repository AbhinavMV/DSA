class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def solve(arr,path):
            if(len(arr)==0):
                results.append(path)
                return
            for i in range(len(arr)):
                solve(arr[:i]+arr[i+1:],path+[arr[i]])
        solve(nums,[])
        return results