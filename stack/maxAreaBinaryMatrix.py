class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0]*len(matrix[0])
        values = []
        for row in matrix:
            for j in range(len(row)):
                if(row[j]=='1'):
                    heights[j] += int(row[j]) 
                else:
                    heights[j] = 0  
            print(heights)
            values.append(self.MAH(heights))
        return max(values)
    
    def MAH(self,arr):
        left = []
        stack = []
        for i in range(len(arr)):
            l = len(stack)
            if(l==0):
                left.append(-1)
            elif(l>0 and stack[-1][0]<arr[i]):
                left.append(stack[-1][1])
            elif(l>0 and stack[-1][0]>=arr[i]):
                while(len(stack)>0 and stack[-1][0]>=arr[i]):
                    stack.pop()
                if(len(stack)==0):
                    left.append(-1)
                else:
                    left.append(stack[-1][1])
            stack.append((arr[i],i))
        
        stack = []
        right = []
        for i in range(len(arr)-1,-1,-1):
            l = len(stack)
            if(l==0):
                right.append(len(arr))
            elif(l>0 and stack[-1][0]<arr[i]):
                right.append(stack[-1][1])
            else:
                while(len(stack)>0 and stack[-1][0]>=arr[i]):
                    stack.pop()
                if(len(stack)==0):
                    right.append(len(arr))
                else:
                    right.append(stack[-1][1])
            stack.append((arr[i],i))
        right = right[::-1]
        width = []
        for i in range(len(arr)):
            width.append((right[i]-left[i]-1)*arr[i])
        return max(width)
        