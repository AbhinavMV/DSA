class Solution:
    def minSteps(self,n:int) -> int:
        if n==1:
            return 0
        if n==2:
            return 2
        dp = [float('inf')]*(n+1)
        dp[1] = 0
        dp[2] = 2
        for i in range(3,n+1):
            for j in range(i-1,0,-1):
                if i % j == 0:
                    if j==1:
                        dp[i] = i
                    else:
                        dp[i] = dp[j]+dp[i//j]
                        break
        return dp[n]

# Recursion using string length
#     def minSteps(self, n:int) -> int:        
#         def solve(currStr,copiedStr):
#             if(currStr>=n):
#                 if(currStr==n):
#                     return 0
#                 return float('inf')
#             op1 = float('inf')
#             op2 = float('inf')
#             if(currStr>copiedStr):
#                 op1 = 1+solve(currStr,currStr)
#             if(copiedStr!=0):
#                 op2 = 1+solve(currStr+copiedStr,copiedStr)
#             return min(op1,op2)
    
#         return solve(1,0)

# Recusion using string comparision (initial thoughts)
#     def minSteps(self, n: int) -> int:
#         currStr = 'A'
#         copiedStr = ''
#         finalStr = 'A'*n
#         t={}
#         def solve(curr,copied):
            
#             curLen = len(curr)
#             copLen = len(copied)
#             key = (curLen,copLen)
#             if key in t:
#                 return t[key]
#             if(curLen>=n):
#                 if(curLen==n):
#                     return 0
#                 return float('inf')
            
#             op1 = float('inf')
#             if(curLen>copLen):
#                 op1 = 1+solve(curr,curr)
#             op2 = float('inf')
#             if(copLen!=0):
#                 op2 = 1+solve(curr+copied,copied) 
#             t[key] = min(op1,op2)
#             return t[key]
        
#         return solve(currStr,copiedStr)
