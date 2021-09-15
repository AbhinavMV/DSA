class Solution:
    def countSubstrings(self, s: str) -> int:    
        global t
        t={}
        return self.solve(s,0,len(s)-1)
    
    def solve(self,s,i,j):
        global t
        key=(i,j)
        if key in t:
            return t[key]
        if(i>j):
            return 0
        if(i==j):
            return 1
        if(self.isPalindrome(s[i:j+1])):
            t[key]= self.solve(s,i+1,j)+self.solve(s,i,j-1)+1-self.solve(s,i+1,j-1)
            return t[key]
        t[key]= self.solve(s,i+1,j)+self.solve(s,i,j-1)-self.solve(s,i+1,j-1)
        return t[key]
        
    def isPalindrome(self,s):
        return s == s[::-1]