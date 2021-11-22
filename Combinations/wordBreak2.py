class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        results = []
        self.solve(s,[],0,wordDict,results)
        return results
    
    def solve(self,s,path,currIndex,wordDict,results):
        if(currIndex==len(s)):
            results.append(' '.join(path))
            return True
        flag=0
        for i in range(currIndex+1,len(s)+1):
            substr = s[currIndex:i]
            if(substr in wordDict and self.solve(s,path+[substr],i,wordDict,results)):
                flag = 1
        return flag==1
        