class Solution:
    #applying binary search twice
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        small = self.OccurenceBS(nums,size,target,True)
        large = self.OccurenceBS(nums,size,target,False)
        return [small,large]
    
    def OccurenceBS(self,nums,size,target,isFirst):
        start = 0
        end = size - 1 
        ans = -1
        while (start<=end):
            mid = (start+end)//2
            if(nums[mid]<target):
                start = mid+1
            elif(nums[mid]>target):
                end = mid-1
            else:
                ans = mid
                if(isFirst):
                    end = mid-1
                else:
                    start = mid+1
        return ans
        
    #Recursive solution
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        global small,large
        small = float('inf')
        large = -1
        n = len(nums)-1
        (self.solve(nums,0,n,target))
        small = small if small!=float('inf') else -1
        large = large if large!=-1 else -1
        return [small,large]
        
    @classmethod
    def solve(self,arr,s,e,target):
        if(s>e):
            return -1
        mid = (s+e)//2
        if(arr[mid]==target):
            global small,large
            small = min(small,mid)
            large = max(large,mid)
        self.solve(arr,s,mid-1,target)
        self.solve(arr,mid+1,e,target)
        return