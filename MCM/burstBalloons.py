class Solution:
    def maxCoins(self,nums: List[int]) -> int:
        arr = [1] + nums + [1]
        size = len(nums)
        t = [[0 for i in range(size+2)] for i in range(size+2)]
        for i in range(1,size+1):
            t[i][i] = arr[i-1]*arr[i]*arr[i+1]
        for g in range(2,size+1):
            i = 1
            for j in range(g,size+1):
                ans = float('-inf')
                for k in range(i,j+1):
                    ans = max(t[i][k-1] + 
                        t[k+1][j]+ 
                        arr[i-1]*arr[k]*arr[j+1],ans)
                    t[i][j] = ans
                i = i+1 
        return t[1][-2]

    #Memoized
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
