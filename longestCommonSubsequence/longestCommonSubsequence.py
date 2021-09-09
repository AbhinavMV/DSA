class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        t = [[-1 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    t[i][j]=0
                elif(text1[i-1]==text2[j-1]):
                    t[i][j] = 1+t[i-1][j-1]
                else:
                    t[i][j] = max(t[i][j-1],t[i-1][j])
        return t[m][n]
        
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m = len(text1)
#         n = len(text2)
#         global t
#         t = {}
#         return self.solve(text1,text2,m,n)
        
#     def solve(self,text1,text2,m,n):
#         global t
#         key = (m,n)
#         if(key in t):
#             return t[key]
#         if(m==0 or n==0):
#             return 0
#         elif(text1[m-1]==text2[n-1]):
#             t[key]= 1+self.solve(text1,text2,m-1,n-1)
#             return t[key]
#         else:
#             t[key]= max(self.solve(text1,text2,m-1,n),self.solve(text1,text2,m,n-1))
#             return t[key]