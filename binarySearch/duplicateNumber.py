class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1
        while (left<=right):
            mid = (left+right)//2
            count = 0
            for i in nums:
                if(i<=mid):
                    count+=1
            if(count>mid):
                duplicate = mid
                right = mid-1
            else:
                left = mid+1
        return duplicate