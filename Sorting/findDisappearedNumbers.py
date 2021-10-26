class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        i=0
        out = []
        while(i<n):
            val = nums[i]-1
            if(val==i):
                i+=1
            elif(nums[val]==val+1):
                i+=1
            elif(nums[val]!=val+1):
                nums[i],nums[val] = nums[val],nums[i]
                
        for i in range(n):
            if(i!=nums[i]-1):
                out.append(i+1)
                
        return out