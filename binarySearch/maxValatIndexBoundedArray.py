class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def check(mid):
            n1 = index+1
            n2 = n-index
            sum1 = mid*(mid+1)/2 + (n1-mid)
            sum2 = mid*(mid+1)/2 + (n2-mid)
            
            if(n1<=mid):
                sum1 = n1/2*(2*mid-n1+1)
            if(n2<=mid):
                sum2 = n2/2*(2*mid-n2+1)
            s = sum1+sum2-mid
            return s<=maxSum
        
        left = 1
        right = maxSum
        while left<right:
            mid = (left+right+1)//2
            if(check(mid)):
                left=mid
            else:
                right=mid-1
        return left