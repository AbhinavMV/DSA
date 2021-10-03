class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        level = len(triangle)
        n = len(triangle[-1])
        t = [[float('inf') for i in range(n+1)] for i in range(level+1)]
        for i in range(1,level+1):
            for j in range(1,n+1):
                temp = min(t[i-1][j-1],t[i-1][j])
                if(temp == float('inf')):
                    temp = 0
                if(j<=len(triangle[i-1])):
                    t[i][j] = triangle[i-1][j-1] + temp
        return min(t[-1])
        
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         size = len(triangle)
#         t = {}
#         def solve(level,idx):
#             key = (level,idx)
#             if key in t:
#                 return t[key]
#             if level==size:
#                 return 0
#             op1 = triangle[level][idx] + solve(level+1,idx)
#             op2 = triangle[level][idx] + solve(level+1,idx+1)
#             t[key] = min(op1,op2)
#             return t[key]
        
#         return solve(0,0) 