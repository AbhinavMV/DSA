class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def solve(start,end):
            key = (start,end)
            if (key in dp):
                return dp[key]
            if(start==end):
                return nums[start]
            dp[key] = max(nums[start]-solve(start+1,end),nums[end]-solve(start,end-1))
            return dp[key]
        
        return solve(0,len(nums)-1) >= 0
    
