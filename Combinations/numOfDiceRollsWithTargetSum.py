class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = {}
        def solve(dice,t):
            key = (dice,t)
            if key in dp:
                return dp[key]
            if(dice<=0 or t<=0):
                if(dice==0 and t==0):
                    return 1
                return 0
            else:
                ans = 0
                for i in range(1,f+1):
                    ans += solve(dice-1,t-i) 
                dp[key] = ans % (10**9 + 7)
                return dp[key]
        return solve(d,target)