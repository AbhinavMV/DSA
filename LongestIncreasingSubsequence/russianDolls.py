import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda val:(val[0],-val[1]))
        
        tails = []
        for w,h in envelopes:
            index = bisect.bisect_left(tails,h)
            if index==len(tails):
                tails.append(h)
            else:
                tails[index] = h
        return len(tails)
        
        
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #     envelopes.sort(key=lambda val:(val[0],-val[1]))
    #     size = len(envelopes)
    #     dp = [1]*size
    #     res = 1
    #     for i in range(size):
    #         for j in range(i):
    #             if(envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]):
    #                 dp[i] = max(dp[i],dp[j]+1)
    #                 res = max(res,dp[i])
    #     return res
    
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    #     global t
    #     t = {}
    #     envelopes.sort(key=lambda val:val[0])
    #     return self.solve(envelopes,-1,0,len(envelopes))
    # def solve(self,arr,prev,curr,size):
    #     global t
    #     key = (prev,curr)
    #     if key in t:
    #         return t[key]
    #     if(curr==size):
    #         return 0
    #     op1 = 0
    #     if(prev==-1 or (arr[curr][0]>arr[prev][0] and arr[curr][1]>arr[prev][1])):
    #         op1 = 1 + self.solve(arr,curr,curr+1,size)
    #     op2 = self.solve(arr,prev,curr+1,size)
    #     t[key] = max(op1,op2)
    #     return t[key]