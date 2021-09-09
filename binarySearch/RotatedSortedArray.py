class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        print(pivot)
        start = 0 
        end = len(nums)-1
        if(pivot!=-1 and nums[pivot]<target):
            return -1
        elif(pivot==-1):
            return self.binarySearch(nums,target,start,end)
        elif(nums[pivot]>=target and nums[start]<=target):
            return self.binarySearch(nums,target,start,pivot)
        else:
            return self.binarySearch(nums,target,pivot+1,end)
        
    @classmethod
    def binarySearch(self,nums,target,start,end):
        while(start<=end):
            mid = (start+end)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                end  = mid-1
            else:
                start=mid+1
        return -1
    
    @classmethod
    def findPivot(self,arr):
        start = 0
        end = len(arr)-1
        while(start<=end):
            mid = (start+end)//2
            if(mid<end and arr[mid]>arr[mid+1]):
                return mid
            if((mid>start and arr[mid]<arr[mid-1])):
                return mid-1
            if(arr[mid]<=arr[start]):
                end=mid-1
            else:
                start=mid+1       
        return -1