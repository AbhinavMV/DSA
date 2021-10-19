class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(mid):
            s = 0
            for i in piles:
                temp = i/mid
                if(temp-int(temp) > 0):
                    temp = int(temp)+1
                s+=temp
            return s<=h
        
        left = 1
        right = max(piles)+1
        
        while left<right:
            mid = (left+right)//2
            if(check(mid)):
                right = mid
            else:
                left = mid+1
        return left