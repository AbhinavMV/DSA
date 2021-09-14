class Solution:   
    def minScoreTriangulation(self, values: List[int]) -> int:
        global t
        t = {}
        return self.solve(values,0,len(values)-1)
    
    def solve(self,values,left,right):
        global t
        key = (left,right)
        if key in t:
            return t[key]
        if(right-left+1<3):
            return 0
        minimum = float('inf')
        for k in range(left+1,right):
            temp = values[left]*values[k]*values[right] + self.solve(values,left,k)+self.solve(values,k,right)
            minimum = min(minimum,temp)
            t[key] = minimum
        return t[key]