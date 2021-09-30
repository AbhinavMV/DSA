class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        size = len(words)
        words.sort(key=lambda val:len(val))
        dp = [1]*size
        words = words[::-1]
        def isPredecessor(word1,word2):
            l1 = len(word1)
            l2 = len(word2)
            diff = abs(l1-l2)==1
            if(not diff): 
                return False
            for i in range(l2):
                a = word2[:i]+word2[i+1:]
                b = word1
                if(a==b and diff):
                    return True
            return False
        if size == 1:
            return 1
        for i in range(size):
            for j in range(i):
                if(isPredecessor(words[i],words[j])):
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)
    
#     def longestStrChain(self, words: List[str]) -> int:
#         size = len(words)
#         words.sort(key=lambda val:len(val))
#         t = {}
#         def isPredecessor(word1,word2):
#             for i in range(len(word2)):
#                 a = word2[:i]+word2[i+1:]
#                 b = word1
#                 if(a==b and abs(len(word1)-len(word2))==1):
#                     return True
#             return False
        
#         def solve(prev,curr):
#             key = (prev,curr)
#             if key in t:
#                 return t[key]
#             if(curr<0):
#                 return 0
#             op1 = 0
#             if(prev==size or isPredecessor(words[curr],words[prev])):
#                 op1 = 1+solve(curr,curr-1)
#             op2 = solve(prev,curr-1)
#             t[key] = max(op1,op2)
#             return t[key]
        
#         return solve(size,size-1)