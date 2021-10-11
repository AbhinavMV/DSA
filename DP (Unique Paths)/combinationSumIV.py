class Solution:
    def combinationSum4(self,nums: List[int],target: int) -> int:
        nums.sort()
        dp = [0]*(target+1)
        dp[0] = 1
        
        for i in range(target+1):
            for j in nums:
                if j<=i:
                    dp[i]+=dp[i-j]
                else:
                    break
        return dp[-1]
          
#     def combinationSum4(self, nums: List[int], target: int) -> int:
#         t={}
#         def solve(s):
#             if s in t:
#                 return t[s]
#             if(s==0):
#                 return 1
#             ans = 0
#             for i in nums:
#                 if(i<=s):
#                     ans += solve(s-i)
#             t[s] = ans
#             return ans
            
#         return solve(target) 