class Solution:
    def findTargetSumWays(self,nums: List[int], target: int) -> int:
        size = len(nums)
        total = sum(nums)
        newTarget = int((total+target)/2)
        if(abs(target)>total or (total+target)%2!=0):
            return 0

        t = [[-1 for i in range(newTarget+1)] for i in range(size+1)]
        
        for i in range(newTarget+1):
            t[0][i] = 0
        t[0][0] = 1
        for i in range(1,size+1):
            for j in range(newTarget+1):
                if(nums[i-1]<=j):
                    t[i][j] = t[i-1][j-nums[i-1]]+t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        return t[size][newTarget]
            # def solve(n,targetSum):
        #     if(n==0):
        #         if targetSum == 0:
        #             return 1
        #         return 0
        #     op1 = 0
        #     if(nums[n-1]<=targetSum):
        #         op1 = solve(n-1,targetSum-nums[n-1])
        #     op2 = solve(n-1,targetSum)
        #     return op1 + op2 
        # return solve(size,newTarget)
        
    
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     t = {}
    #     def solve(n,currSum):
    #         key = (n,currSum)
    #         if key in t:
    #             return t[key]
    #         if n==0:
    #             if currSum == target:
    #                 return 1
    #             return 0
    #         t[key] = solve(n-1,currSum+nums[n-1])+solve(n-1,currSum-nums[n-1])
    #         return t[key]
    #     op = solve(len(nums),0)
    #     # for i in t:
    #     #     print(t)
    #     return op
        