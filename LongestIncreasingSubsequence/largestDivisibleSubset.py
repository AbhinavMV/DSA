class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        size = len(nums)
        arr = sorted(nums)
        dp = [[0,[]] for i in arr]
        for i in range(size):
            for j in range(i):
                if(arr[i]%arr[j]==0):
                    # print(arr[i],arr[j])
                    if(dp[j][0]>dp[i][0]):
                        # print(dp[j][0],dp[i][0])
                        dp[i][0] = dp[j][0]
                        dp[i][1] = dp[j][1][:]
            dp[i][1].append(arr[i])
            dp[i][0] = len(dp[i][1])
            # print(arr[i],dp[i])
        return max(dp)[1]
#     def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
#         global sol,t
#         sol = []
#         t={}
#         arr = sorted(nums)
#         self.solve(arr,-1,0,len(nums),[])
#         ans = [0,[]]
#         for i in sol:
#             if i[0]>ans[0]:
#                 ans = i
#         return ans[1]
    
#     def solve(self,arr,prev,curr,size,temp):
#         global sol,t
#         key=(prev,curr,len(temp))
#         if(key in t):
#             return t[key]
#         if(curr==size):
#             sol.append([len(temp),temp])
#             return 0
#         op1=0
#         if(prev==-1 or (arr[curr]%arr[prev]==0)):
#             op1 = 1+self.solve(arr,curr,curr+1,size,temp+[arr[curr]])
#         op2 = self.solve(arr,prev,curr+1,size,temp)
#         t[key] = max(op1,op2)
#         return t[key]
        