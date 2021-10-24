class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        s = 0
        e = len(nums)-1
        
        while (s<=e):
            while(nums[s]%2==0 and s<e):
                s+=1
            while(nums[e]%2!=0 and e>s):
                e-=1
            if(s<=e):
                nums[s],nums[e] = nums[e],nums[s]
                s+=1
                e-=1
        return nums