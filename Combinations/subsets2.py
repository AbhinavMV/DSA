class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        def solve(path,start):
            # if(path not in results):
            #     results.append(path)
            results.append(path)
            for i in range(start,len(nums)):
                if(i>start and nums[i-1]==nums[i]):
                    continue
                path.append(nums[i])
                solve(path[:],i+1)
                path.pop()
        cur = []
        solve(cur,0)
        return results