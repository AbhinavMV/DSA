class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size = len(nums)
        if(size==1): 
            return 0
        if(nums[0]>nums[1]):
            return 0
        if(nums[-1]>nums[-2]):
            return size-1
        
        left = 0
        right = size-1
        
        while left<=right:
            mid=(left+right)//2
            if(nums[mid-1]<nums[mid]>nums[mid+1]):
                return mid
            elif(nums[mid-1]>nums[mid]):
                right = mid-1
            elif(nums[mid+1]>nums[mid]):
                left = mid+1
        return -1