class Solution:
    def numSquares(self,n:int)->int:
        dp = [0]*(n+1)
        dp[1] = 1
        
        for i in range(2,n+1):
            ans = float('inf')
            j = 1
            while(j*j<=i):
                ans = min(ans,dp[i-j*j])
                j=j+1
            dp[i] = ans+1
        return dp[n]
    # def numSquares(self, n: int) -> int:
    #     t= {}
    #     def solve(n):
    #         if n in t:
    #             return t[n]
    #         if(n<0):
    #             return float('inf')
    #         if(n==0):
    #             return 0
    #         ans = n
    #         for i in range(1,n):
    #             ans = min(ans,1+solve(n-i*i))
    #         t[n] = ans
    #         return t[n]
    #     return solve(n)
    
#     def numSquares(self, n: int) -> int:
        
#         num = 1
#         square = 1
#         arr = []
        
#         while square<=10000:
#             arr.append(square)
#             num+=1
#             square = num**2
        
#         tSize = 0
#         for i in arr:
#             if i>n:
#                 break
#             tSize+=1        
#         t = [[float('inf') for i in range(n+1)] for i in range(tSize+1)]
        
#         for i in range(1,tSize+1):
#             for j in range(0,n+1):
#                 if(j==0):
#                     t[i][j]=0  
#                 elif(arr[i-1]<=j):
#                     t[i][j] = min(1+t[i][j-arr[i-1]],t[i-1][j])
#                 else:
#                     t[i][j] = t[i-1][j]
#         return t[tSize][n]
        
    
#     def numSquares(self, n: int) -> int:
        
#         num = 1
#         square = 1
#         arr = []
        
#         while square<=10000:
#             arr.append(square)
#             num+=1
#             square = num**2
#         tSize = len(arr)
#         t ={} 
        
#         def solve(curr,target):
#             key = (curr,target)
#             if key in t:
#                 return t[key]
#             if(curr==tSize or arr[curr]>target or target<=0):
#                 if(target==0):
#                     return 0
#                 return float('inf')
#             op1 = float('inf')
#             op2 = float('inf')
#             if(arr[curr]<=target):
#                 op1 = 1+solve(curr,target-arr[curr])
#                 op2 = solve(curr+1,target)
#             t[key] = min(op1,op2)
#             return t[key]          
#         return solve(0,n)
                