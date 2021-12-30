class Solution:
    def subarraysWithKDistinct(self,s: List[int],k: int) -> int:
        if(len(s)<k):
            return 0
        return self.atMostSubarrays(s,k) - self.atMostSubarrays(s,k-1)
    
    def atMostSubarrays(self,arr: List[int],k: int):
        left,right=0,0
        ans = 0
        hmap = {}
        while(right<len(arr)):
            if(arr[right] in hmap):
                hmap[arr[right]]+=1
            else:
                hmap[arr[right]]=1
            if(len(hmap)<=k):
                ans+= right-left+1
                right+=1
            else:
                while(left<=right and len(hmap)>k):
                    hmap[arr[left]]-=1
                    if(hmap[arr[left]]==0):
                        del hmap[arr[left]]
                    left+=1
                if(len(hmap)<=k):
                    ans+=right-left+1
                right+=1
        return ans   
    
    # Brute Force
    # def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
    #     result = 0
    #     for i in range(len(nums)):
    #         hmap = {}
    #         for j in range(i,len(nums)):
    #             if(nums[j] in hmap):
    #                 hmap[nums[j]]+=1
    #             else:
    #                 hmap[nums[j]]=1
    #             if(len(hmap)==k):
    #                 result+=1
    #     return result
        