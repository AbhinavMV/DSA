class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        size = len(arr)
        t = [[0 for i in range(size)] for i in range(size)]
        
        for g in range(1,size):
            i = 0
            for j in range(g,size):
                if(g==1):
                    t[i][j] = arr[i]*arr[j]
                else:
                    ans = float('inf')
                    for k in range(i,j):
                        product = max(arr[i:k+1])*max(arr[k+1:j+1])
                        temp = product + t[i][k] + t[k+1][j]
                        ans = min(ans,temp)
                    t[i][j]=ans
                i=i+1
        return t[0][-1]
        
#       Memoized 
#     def mctFromLeafValues(self, arr: List[int]) -> int:
#         global t
#         t = {}
#         return self.solve(arr,0,len(arr)-1)
    
#     def solve(self,arr,l,r):
#         global t
#         key = (l,r)
#         if key in t:
#             return t[key]
#         if(l>=r):
#             return 0
#         ans = float('inf')
#         for k in range(l,r):
#             product = max(arr[l:k+1])*max(arr[k+1:r+1])
#             temp = product + self.solve(arr,l,k)+self.solve(arr,k+1,r)
#             ans = min(ans,temp)
#         t[key] = ans
#         return ans
        