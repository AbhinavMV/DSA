class Solution:
    #Sliding window
    def longestSubstring(self,s: str,k: int) -> int:
        hmap = {}
        #calculate all unique characters
        for i in s:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        max_unique = len(hmap)
        result = 0
        #traverse over the whole and try to find the max length substring with current no. of unique characters
        #Then find the max between all these
        for curr_unique in range(1,max_unique+1):
            countmap = {}
            i,j,unique,countAtLeastK=0,0,0,0
            #Use sliding window to find max substring with current number of unique characters.
            while(j<len(s)):
                if(unique<=curr_unique):
                    if(s[j] not in countmap):
                        unique+=1
                        countmap[s[j]]=1
                    else:
                        countmap[s[j]]+=1
                    if(countmap[s[j]]==k):
                        countAtLeastK+=1
                    j+=1
                else:
                    countmap[s[i]]-=1
                    if(countmap[s[i]]==0):
                        unique-=1
                        del countmap[s[i]]
                    elif(countmap[s[i]]==k-1):
                        countAtLeastK-=1
                    i+=1
                if(unique==curr_unique and len(countmap)==countAtLeastK):
                    result = max(j-i,result)
        return result
                    
    # Two pointer approach - Divide and conquer
    # def longestSubstring(self, s: str,k: int) -> int:
    #     hmap = {}
    #     #create hashmap
    #     for i in s:
    #         if i in hmap:
    #             hmap[i]+=1
    #         else:
    #             hmap[i]=1
    #     max_unique = len(hmap)
    #     noKChar = 0
    #     for i in hmap:
    #         if(hmap[i]<k):
    #             noKChar += 1
    #     left = 0
    #     n = len(s)
    #     if(k==0 or k==1 or noKChar==0):
    #         return len(s)
    #     if(k>n):
    #         return 0
    #     while(left<n and hmap[s[left]]>=k):
    #         left+=1
    #     ss1 = self.longestSubstring(s[0:left],k)
    #     ss2 = self.longestSubstring(s[left+1:],k) if left<n else 0
    #     return max(ss1,ss2)
        
    # Brute Force - Accepted
    # def longestSubstring(self, s: str, k: int) -> int:
    #     m=0
    #     for i in range(len(s)):
    #         hmap = {}
    #         for j in range(i,len(s)):
    #             if s[j] in hmap:
    #                 hmap[s[j]]+=1
    #             else:
    #                 hmap[s[j]]=1
    #             flag = False
    #             for p in hmap:
    #                 if(hmap[p]<k):
    #                     flag=True
    #                     break
    #             if(flag==False):
    #                 if(j-i+1>m):
    #                     m = j-i+1
    #     return m