class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        t = [[-1 for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if(i==0 or j==0):
                    t[i][j]=0
                elif(str1[i-1]==str2[j-1]):
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j],t[i][j-1])        
        a = m
        b = n
        result = ''
        while(a>0 and b>0):
            if(str1[a-1]==str2[b-1]):
                result=str1[a-1]+result
                a = a-1
                b = b-1
            else:
                if(t[a-1][b]>t[a][b-1]):
                    result=str1[a-1] + result
                    a=a-1
                else:
                    result=str2[b-1] + result
                    b=b-1
        while(a>0):
            result = str1[a-1] + result
            a =a-1
        while(b>0):
            result = str2[b-1] + result
            b=b-1
        return result