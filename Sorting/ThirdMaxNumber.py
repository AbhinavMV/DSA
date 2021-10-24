class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        size = len(nums)
        #bubble sort
#         for i in range(size):
#             swap = True
#             for j in range(0,size-i-1):
#                 if(nums[j]>nums[j+1]):
#                     nums[j],nums[j+1] = nums[j+1],nums[j]
#                     swap = False
#             if swap:
#                 break
                
        #selection sort
        # for i in range(size):
        #     m = i
        #     for j in range(i,size):
        #         if(nums[i]>nums[j]):
        #             m = j
        #     if(m!=i):
        #         nums[i],nums[m] = nums[m],nums[i]
        
        #insertion sort
        # for i in range(size-1):
        #     j = i+1
        #     while(j>0 and nums[j]<nums[j-1]):
        #         nums[j],nums[j-1] = nums[j-1],nums[j]
        #         j-=1
        
        
        #Merge Sort
        
#         def merge(arr1=[],arr2=[]):
#             n = len(arr1)
#             m = len(arr2)
#             arr3 = []
#             ptr1 = ptr2 = 0
#             while(ptr1<n and ptr2<m):
#                 if(arr1[ptr1]<arr2[ptr2]):
#                     arr3.append(arr1[ptr1])
#                     ptr1+=1
#                 else:
#                     arr3.append(arr2[ptr2])
#                     ptr2+=1
#             for i in range(ptr1,n):
#                 arr3.append(arr1[i])
#             for i in range(ptr2,m):
#                 arr3.append(arr2[i])
#             return arr3
#         def mergeSort(array):
#             n = len(array)
#             if(n==1):
#                 return array
#             mid = n//2
#             l = mergeSort(array[:mid])
#             r = mergeSort(array[mid:])
#             return merge(l,r)
        
#         nums = mergeSort(nums)
        
        #Quick Sort
        
        def sort(array,left,right):
            if(left>=right):
                return 
            start = left
            end = right
            mid = (start+end)//2
            pivot = array[mid]
            while(start<=end):
                while(array[start]<pivot):
                    start+=1
                while(array[end]>pivot):
                    end-=1
                if(start<=end):
                    array[start],array[end] = array[end],array[start]
                    start+=1
                    end-=1
            sort(array,left,end)
            sort(array,start,right)
        sort(nums,0,size-1)    
        print(nums)
        count=1
        for j in range(size-2,-1,-1):
            if(nums[j]!=nums[j+1]):
                count+=1
            if(count==3):
                return nums[j]
        return nums[-1]