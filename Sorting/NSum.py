class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        def solve(arr,t,N,p,results):
            size = len(arr)
            if(size<N or N<2 or t<N*arr[0] or t>N*arr[-1]):
                return
            if(N==2):
                # 2sum
                left , right = 0,size-1
                while(left<right):
                    temp = arr[left]+arr[right]
                    if(temp==t):
                        li = p+[arr[left],arr[right]]
                        results.append(li)
                        left+=1
                        while(left<right and arr[left]==arr[left-1]):
                            left+=1
                    elif(temp<t):
                        left+=1
                    else:
                        right-=1
            else:
                for i in range(size-N+1):
                    if(i==0 or (i>0 and arr[i]!=arr[i-1])):
                        solve(arr[i+1:],t-arr[i],N-1,p+[arr[i]],results)
                        
                        
        N = 4
        results = []
        solve(sorted(nums),target,N,[],results)
        return results
            
        