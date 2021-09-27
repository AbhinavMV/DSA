class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda val:(val[0],val[1]))
        size = len(pairs)
        dp = [1]*size
        res = 1
        if size==1:
            return 1
        for i in range(size):
            for j in range(i):
                if(pairs[i][0]>pairs[j][1]):
                    dp[i] = max(dp[i],dp[j]+1)
                    res = max(res,dp[i])
        return res
    
#     def findLongestChain(self, pairs: List[List[int]]) -> int:
#         pairs.sort(key= lambda val:(val[0],val[1]))
#         global t
#         t = {}
#         return self.solve(pairs,-1,0,len(pairs))
    
#     def solve(self,arr,prev,curr,size):
#         global t
#         key = (prev,curr)
#         if key in t:
#             return t[key]
#         if(curr==size):
#             return 0
#         op1=0
#         if(prev==-1 or arr[prev][1]<arr[curr][0]):
#             op1 = 1 + self.solve(arr,curr,curr+1,size)
#         op2 = self.solve(arr,prev,curr+1,size)
#         t[key] = max(op1,op2)
#         return t[key]