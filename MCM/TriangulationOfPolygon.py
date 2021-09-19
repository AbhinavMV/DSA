class Solution:   
    def minScoreTriangulation(self, values: List[int]) -> int:
        size = len(values)
        t = [[0 for i in range(size)] for i in range(size)]
        for g in range(2,size):
            i = 0
            for j in range(g,size):
                ans = float('inf')
                for k in range(i+1,j):
                    currTriangle = values[i]*values[k]*values[j]
                    temp = currTriangle + t[i][k] + t[k][j]
                    ans = min(ans,temp)
                    t[i][j] = ans
                i = i+1
        return t[0][-1]
    
    #Memoized solution
#     def minScoreTriangulation(self, values: List[int]) -> int:
#         global t
#         t = {}
#         return self.solve(values,0,len(values)-1)
    
    
#     def solve(self,values,left,right):
#         global t
#         key = (left,right)
#         if key in t:
#             return t[key]
#         if(right-left+1<3):
#             return 0
#         minimum = float('inf')
#         for k in range(left+1,right):
#             temp = values[left]*values[k]*values[right] + self.solve(values,left,k)+self.solve(values,k,right)
#             minimum = min(minimum,temp)
#             t[key] = minimum
#         return t[key]