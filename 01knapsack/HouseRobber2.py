class Solution:
    def rob(self,nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        elif size == 2:
            return max(nums)
        
        def getMax(arr):
            l = len(arr)
            dp = [0]*l
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])
            for i in range(2,l):
                dp[i] = max(dp[i-1],arr[i]+dp[i-2])
            
            return dp[-1]
        return max(getMax(nums[0:size-1]),getMax(nums[1:size]))
        
#     def rob(self, nums: List[int]) -> int:
#         size = len(nums)
#         if size == 1:
#             return nums[0]
#         if size == 2:
#             return max(nums)
        
#         def solve(arr,curr,t):
#             if curr>=len(arr):
#                 return 0
#             if curr in t:
#                 return t[curr]
#             t[curr] = max(arr[curr]+solve(arr,curr+2,t),solve(arr,curr+1,t))
#             return t[curr]
#         return max(solve(nums[0:size-1],0,{}),solve(nums[1:size],0,{}))
        