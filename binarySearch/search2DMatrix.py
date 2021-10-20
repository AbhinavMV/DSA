class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        
        while (top<bottom):
            midv = (top+bottom)//2
            # print('outer',matrix[midv][0],target,matrix[midv][right-1])
            if(matrix[midv][0]<=target<=matrix[midv][right-1]):
                while(left<right):
                    midh=(left+right+1)//2                                            
                    # print('inner',matrix[midv][midh-1],target)
                    if(matrix[midv][midh-1]==target):
                        return True
                    elif(matrix[midv][midh-1]>target):
                        right = midh-1
                    else:
                        left = midh
            elif(matrix[midv][right-1]>target):
                bottom = midv
            else:
                top = midv+1
        return False