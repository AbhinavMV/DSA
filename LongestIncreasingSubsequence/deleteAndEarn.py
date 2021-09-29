class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        arr = [0] * (max(nums)+1)
        for i in nums:
            arr[i]+=i
        # print(arr)
        size = len(arr)
        t = {}
        def solve(curr):
            if curr in t:
                return t[curr]
            if(curr>=size):
                return 0
            op1 = arr[curr] + solve(curr+2)
            op2 = solve(curr+1)
            t[curr] = max(op1,op2)
            return t[curr]
        return solve(0)