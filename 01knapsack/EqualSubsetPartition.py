class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        subsetSum = totalSum//2
        if(totalSum%2 != 0):
            return False
        return self.solve(nums,len(nums),subsetSum)==subsetSum
    #dp
    @classmethod
    def solve(self,arr,N,S):
        t = [[-1 for i in range(S+1)] for i in range(N+1)]
        for n in range(N+1):
            for s in range(S+1):
                if(s==0 or n==0):
                    t[n][s] = 0
                elif(arr[n-1]<=s):
                    t[n][s] = max(arr[n-1]+t[n-1][s-arr[n-1]],t[n-1][s])
                else:
                    t[n][s] = t[n-1][s]
        return t[N][S]
    
#     #memoised or top down approach
#     @classmethod
#     def solve(self,arr,N,S):
#         global t
#         key = (N,S)
#         if(N==0 or S==0):
#             return 0
#         if(key in t):
#             return t[key]
#         elif(arr[N-1]<=S):
#             t[key] = max(arr[N-1]+self.solve(arr,N-1,S-arr[N-1]),self.solve(arr,N-1,S))
#             return t[key]
#         t[key] = self.solve(arr,N-1,S)
#         return t[key]
    
    #recursive  
    # @classmethod
    # def solve(self,arr,N,S):
    #     if(N==0 or S==0):
    #         return 0
    #     elif(arr[N-1]<=S):
    #         return max(arr[N-1]+self.solve(arr,N-1,S-arr[N-1]),self.solve(arr,N-1,S))
    #     else:
    #         return self.solve(arr,N-1,S)