class Solution:
    def trap(self, height: List[int]) -> int:
        left = [height[0]]
        right = [height[-1]]
        maxVal = height[0]
        for i in range(1,len(height)):
            if(height[i]>maxVal):
                maxVal=height[i]
            left.append(maxVal)
        maxVal = right[0]
        for i in range(len(height)-2,-1,-1):
            if(height[i]>maxVal):
                maxVal = height[i]
            right.append(maxVal)
        right = right[::-1]
        ts = 0
        for i in range(len(height)):
            temp = min(right[i],left[i])-height[i]
            if(temp>0):
                ts+= temp 
        return ts