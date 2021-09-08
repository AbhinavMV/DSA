class Solution:
    @classmethod
    def find0and1(self,element):
        zero = 0
        one = 0
        for i in element:
            if int(i)==1:
                one=one+1
            else:
                zero = zero+1
        return (zero,one)
        
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arrLen = len(strs)
        temp = {}
        t = [[[-1 for i in range(arrLen+1)] for i in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                for k in range(arrLen+1):
                    if((i==0 and j==0) or k==0):
                        t[i][j][k] = 0
                    else:
                        if(strs[k-1] in temp):
                            x,y = temp[strs[k-1]]
                        else:
                            x,y = self.find0and1(strs[k-1])
                            temp[strs[k-1]] = (x,y)
                        if(x<=i and y<=j):
                            t[i][j][k] = max(1+t[i-x][j-y][k-1],t[i][j][k-1])
                        else:
                            t[i][j][k] = t[i][j][k-1]
                            
        return t[m][n][arrLen]

#         global t 
#         t = {}
#         temp = self.solve(strs,arrLen,m,n)
#         return temp
    
    #memoised solution
    @classmethod
    def solve(self,arr,arrLen,m,n):
        global t
        key = (arrLen,m,n)
        if(key in t):
            return t[key]
        if(arrLen==0 or(m<=0 and n<=0)):
            return 0
        x,y = self.find0and1(arr[arrLen-1])
        if(x<=m and y<=n):
            t[key] = max(1+self.solve(arr,arrLen-1,m-x,n-y),self.solve(arr,arrLen-1,m,n))
            return t[key]
        t[key] = self.solve(arr,arrLen-1,m,n)
        return t[key]
    
