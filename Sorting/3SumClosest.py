class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            left = i+1
            right = n-1
            while (left<right):
                curr = nums[i] + nums[right] +nums[left]
                if(abs(curr-target)<abs(res-target)):
                    res = curr
                elif(curr>target):
                    right-=1
                elif(curr<target):
                    left+=1
                else:
                    return res
        return res