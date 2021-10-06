class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [1]*size
        count = [1]*size
        
        for i in range(1,size):
            for j in range(i):
                if(nums[j]<nums[i]):
                    if(dp[j]+1>dp[i]):
                        dp[i] = dp[j]+1
                        count[i]=count[j]
                    elif(dp[j]+1==dp[i]):
                        count[i]+=count[j]
        length = max(dp)
        c = 0
        for i in range(size):
            if dp[i] == length:
                c+= count[i]                  
        return c