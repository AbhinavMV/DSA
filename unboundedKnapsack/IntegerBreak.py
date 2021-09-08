class Solution:
    def integerBreak(self, n: int) -> int:
        arr = [i for i in range(1,n)]
        arrLen = len(arr)
        t = [[-1 for i in range(n+1)] for i in range(arrLen+1)]
        for i in range(arrLen+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    t[i][j] = 1
                elif(arr[i-1]<=j):
                    t[i][j] = max(arr[i-1]*t[i][j-arr[i-1]],t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[arrLen][n]
        
#       memoised 
#     @classmethod
#     def solve(self,arr,n,s):
#         global t
#         key=(n,s)
#         if(key in t):
#             return t[key]
#         if(n==0 or s==0):
#             return 1
#         if(arr[n-1]<=s):
#             t[key]= max(arr[n-1]*self.solve(arr,n,s-arr[n-1]),self.solve(arr,n-1,s))
#             return t[key]
#         t[key]= self.solve(arr,n-1,s)
#         return t[key]
    
#     def integerBreak(self, n: int) -> int:
#         arr = [i for i in range(1,n)]
#         global t
#         t = {}
#         temp = self.solve(arr,len(arr),n)
#         return temp
    
        