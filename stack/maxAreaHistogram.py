class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        values1 = []
        #Nearest Smallest to Left
        for i in range(0,len(heights)):
            l = len(stack)
            if(l==0):
                values1.append(i-(-1))
            elif(l>0 and stack[-1][0]<heights[i]):
                values1.append(i-stack[-1][1])
            elif(l>0 and stack[-1][0]>=heights[i]):
                while(len(stack) and stack[-1][0]>=heights[i]):
                    stack.pop()
                if(len(stack)==0):
                    values1.append(i-(-1))
                else:
                    values1.append(i-stack[-1][1])
            stack.append((heights[i],i))
        stack = []
        values2 = []
        #Nearest Smallest to Right
        for i in range(len(heights)-1,-1,-1):
            l = len(stack)
            if(l==0): 
                values2.append(-1)
            elif(l>0 and stack[-1][0]<heights[i]):
                values2.append(stack[-1][1])
            elif(l>0 and stack[-1][0]>=heights[i]):
                while(len(stack) and stack[-1][0]>=heights[i]):
                    stack.pop()
                if(len(stack)==0):
                    val = len(heights) - ((len(heights)-i)-1) -1  
                    values2.append(-1)
                else:
                    values2.append(stack[-1][1])
            stack.append((heights[i],i))
        temp = []
        values2 = values2[::-1]
        for i in range(len(heights)):
            if(values2[i]!=-1):
                values2[i] = values2[i]-i
            else:
                values2[i] = len(heights)-i
        area = []
        for i in range(len(heights)):
            area.append(abs(values1[i]+values2[i])*heights[i] - heights[i])
        return max(area)