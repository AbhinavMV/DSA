class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        dp = [[0 for i in range(l2+1)] for i in range(l1+1)]
        for i in range(0,l2+1):
            dp[0][i] = 0 
        for i in range(0,l1+1):
            dp[i][0] = 1
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if(s[i-1]==t[j-1]):
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[l1][l2]

#         global temp
#         temp = {}
#         return self.solve(s,t)
        
#     def solve(self,s,t):
#         global temp
#         key = (s,t)
#         if (key in temp):
#             return temp[key]
#         if(t==''):
#             return 1
#         if(s==''):
#             return 0
#         if(s[0]==t[0]):
#             temp[key] = self.solve(s[1:],t[1:])+self.solve(s[1:],t)
#             return temp[key]
#         else:
#             temp[key] = self.solve(s[1:],t)
#             return temp[key]