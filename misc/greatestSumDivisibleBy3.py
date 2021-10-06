class Solution:
    def maxSumDivThree(self,nums: List[int]) -> int:
        size = len(nums)
        t = {}
        
        def solve(idx,remainder):
            key = (idx,remainder)
            if key in t:
                return t[key]
            
            if idx == size:
                if remainder == 0:
                    return 0
                return float('-inf')
            
            op1 = nums[idx] + solve(idx+1,(remainder + nums[idx])%3)
            op2 = solve(idx+1,remainder)
            t[key] = max(op1,op2)
            return t[key]
        ans = solve(0,0)
        return 0 if ans==float('-inf') else ans
        
                
#    def maxSumDivThree(self, nums: List[int]) -> int:
#         size = len(nums)
#         t = {}
        
#         def solve(idx,currSum):
#             key = (idx,currSum)
#             if key in t:
#                 return t[key]
            
#             if idx == size:
#                 if currSum % 3 == 0:
#                     return currSum
#                 return 0
            
#             op1 = solve(idx+1,currSum+nums[idx])
#             op2 = solve(idx+1,currSum)
#             t[key] = max(op1,op2)
#             return t[key]
        
#         return solve(0,0)
        