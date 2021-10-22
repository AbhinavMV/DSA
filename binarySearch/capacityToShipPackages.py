class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        def check(tcapacity):
            s,count = 0,1
            for i in weights:
                s+=i
                if(s>=tcapacity):
                    s = i
                    count+=1
            if(count<=days):
                return True
            return False
        
        while(left<right):
            mid = (left+right+1)//2
            if(check(mid)):
                right = mid-1
            else:
                left = mid
        return left