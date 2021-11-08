class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        def solve(arr,path):
            if(len(arr)==0):
                results.append(path)
                return
            for i in range(len(arr)):
                if(i!=0 and arr[i]==arr[i-1]):
                    continue
                solve(arr[:i]+arr[i+1:],path+[arr[i]])
        solve(nums,[])
        return results