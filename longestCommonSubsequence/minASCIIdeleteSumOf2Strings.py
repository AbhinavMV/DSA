class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        t = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            t[i][0] = t[i-1][0] + ord(s1[i-1])
        for j in range(1,n+1):
            t[0][j] = t[0][j-1] + ord(s2[j-1])
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(s1[:i]==s2[:j]):
                    t[i][j] = 0
                elif(s1[i-1]==s2[j-1]):
                    t[i][j] = t[i-1][j-1]
                else:
                    first = ord(s1[i-1])
                    second = ord(s2[j-1])
                    case1 = t[i-1][j] + first
                    case2 = t[i][j-1] + second
                    case3 = t[i-1][j-1] + first + second
                    t[i][j] = min(case1,case2,case3)
        return t[m][n]

    #   recursion and memoized
    #     global t
    #     t = {}
    #     return self.solve(s1,s2,len(s1),len(s2))
    # def solve(self,s1,s2,m,n):
    #     global t
    #     key = (m,n)
    #     if(key in t):
    #         return t[key]
    #     if(m==0):
    #         temp = 0
    #         for i in range(n):
    #             temp += ord(s2[i])
    #         return temp
    #     if(n==0):
    #         temp = 0
    #         for i in range(m):
    #             temp += ord(s1[i])
    #         return temp
    #     if(s1[:m]==s2[:n]):
    #         return 0
    #     if(s1[m-1]==s2[n-1]):
    #         t[key] = self.solve(s1,s2,m-1,n-1)
    #         return t[key]
    #     first = ord(s1[m-1])
    #     second = ord(s2[n-1])
    #     case1 = self.solve(s1,s2,m-1,n) + first
    #     case2 = self.solve(s1,s2,m,n-1) + second
    #     case3 = self.solve(s1,s2,m-1,n-1) + first + second
    #     t[key] = min(case1,case2,case3)
    #     return t[key]   