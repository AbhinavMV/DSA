class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        t = [[-1 for i in range(l2+1)] for i in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if(i==0):
                    t[i][j] = j
                elif(j==0):
                    t[i][j] = i
                elif(word1[i-1]==word2[j-1]):
                    t[i][j] = t[i-1][j-1]
                else:
                    t[i][j] = 1+min(t[i-1][j],t[i][j-1],t[i-1][j-1])
        return t[l1][l2]
        
#Memoised        
#         global t
#         t = {}
#         return self.find(word1,word2)
    
#     def find(self,word1,word2):
#         global t
#         key = (word1,word2)
#         if(key in t):
#             return t[key]
#         l1 = len(word1)
#         l2 = len(word2)
#         if(l1==0 and l2==0):
#             return 0
#         if(l1==0):
#             return l2
#         if(l2==0):
#             return l1
#         if(word1[-1]==word2[-1]):
#             t[key]= self.find(word1[:l1-1],word2[:l2-1])
#             return t[key]
#         insert = 1 + self.find(word1,word2[:l2-1])
#         delete = 1 + self.find(word1[:l1-1],word2)
#         replace = 1 + self.find(word1[:l1-1],word2[:l2-1])
#         t[key]= min(insert,delete,replace)
#         return t[key]