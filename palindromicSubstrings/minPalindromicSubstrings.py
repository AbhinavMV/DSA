class Solution:
    def minCut(self, s: str) -> int:
        global t
        t={}
        return self.solve(s,0,len(s)-1)
    
    def isPalindrome(self,s,i,j):
        return s[i:j+1]==s[i:j+1][::-1]
    
    def solve(self,s,i,j):
        global t
        key = (i,j)
        if(key in t):
            return t[key]
        if(i>j):
            return 0
        if(self.isPalindrome(s,i,j)):
            return 0
        ans = float('inf')
        for k in range(i,j+1):
            if(self.isPalindrome(s,i,k)):
                temp = 1 + self.solve(s,k+1,j)
                ans = min(ans,temp)
        t[key]=ans
        return ans