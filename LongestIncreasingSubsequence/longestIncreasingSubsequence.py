class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1]*size
        
        for i in range(size):
            for j in range(i):
                if(nums[j]<nums[i]):
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)
                
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         global t
#         t={}
#         return self.solve(nums,-1,0,len(nums))
    
#     def solve(self,nums,prev,curr,size):
#         key = (prev,curr)
#         if(key in t):
#             return t[key]
#         if(curr==size):
#             return 0
#         op1 = 0
#         if(prev==-1 or nums[prev]<nums[curr]):
#             op1 = 1+self.solve(nums,curr,curr+1,size)
#         op2 = self.solve(nums,prev,curr+1,size)
#         t[key] = max(op1,op2)
#         return t[key]
        
        