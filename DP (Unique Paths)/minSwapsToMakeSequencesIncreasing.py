class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        size = len(nums1)
        swap = [0]*size
        not_swap = [0]*size
        swap[0] = 1 
        for i in range(1,size):
            not_swap[i] = float('inf')
            swap[i] = float('inf')
            if(nums1[i]>nums1[i-1] and nums2[i]>nums2[i-1]):
                not_swap[i] = not_swap[i-1]
                swap[i] = swap[i-1]+1
            if(nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]):
                not_swap[i] = min(not_swap[i],swap[i-1])
                swap[i] = min(not_swap[i-1]+1,swap[i])
        return min(not_swap[-1],swap[-1])
#     def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
#         size = len(nums1)
#         ans = size
#         def solve(i,swaps):
#             nonlocal ans
#             if(swaps>ans):
#                 return
#             if(i==size):
#                 ans = min(ans,swaps)
#                 return
#             if(nums1[i]>nums1[i-1] and nums2[i]>nums2[i-1]):
#                 solve(i+1,swaps)
#             if(nums1[i]>nums2[i-1] and nums2[i]>nums1[i-1]):
#                 nums1[i],nums2[i] = nums2[i],nums1[i]
#                 solve(i+1,swaps+1)
#                 nums1[i],nums2[i] = nums2[i],nums1[i]

#         solve(1,0)
#         return ans
