class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        left = 0
        right = n-1
        while(left<=right):
            cmid = (left+right)//2
            
            ridx , cMax = 0,float('-inf')
            for i in range(m):
                if(mat[i][cmid]>cMax):
                    cMax = mat[i][cmid]
                    ridx = i
            
            leftSideBig = cmid>left and mat[ridx][cmid-1]>mat[ridx][cmid]
            rightSideBig = cmid<right and mat[ridx][cmid+1]>mat[ridx][cmid]
            
            if(not leftSideBig and not rightSideBig):
                return [ridx,cmid]
            elif(leftSideBig):
                right = cmid-1
            else:
                left = cmid+1
        return [-1,-1]
        
        
