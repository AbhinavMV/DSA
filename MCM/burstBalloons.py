class Solution:
    #*****NOT OPTIMIZED*****
    def maxCoins(self, nums: List[int]) -> int:
        global t
        t = {}
        sol = [1]+nums+[1]
        return self.solve(sol,1,len(sol)-2)

    def solve(self,nums,i,j):
        global t
        key = (i,j)
        if key in t:
            return t[key]
        if(i>j):
            return 0
        ans = 0
        for k in range(i,j+1):
            left = nums[i-1]
            middle = nums[k]
            right = nums[j+1]
            temp = (left*middle*right) + self.solve(nums,i,k-1) + self.solve(nums,k+1,j)
            ans = max(ans,temp)    
        t[key] = ans
        return t[key]     
