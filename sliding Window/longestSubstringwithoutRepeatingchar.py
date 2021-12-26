class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        i,j = 0,0
        ans = 0
        while(j<len(s)):
            if(s[j] not in hmap):
                ans = max(ans,j-i+1)
            else:
                if(i<=hmap[s[j]]<j):
                    i=hmap[s[j]]+1
                else:
                    ans = max(ans,j-i+1)
            hmap[s[j]] = j
            j+=1
        return ans
    
#     def lengthOfLongestSubstring(self, s: str) -> int:
        
#         i,j = 0,0
#         ans,m = 0,0
#         hmap = {}
#         while(j<len(s)):
#             if(s[j] in hmap):
#                 hmap[s[j]]+=1
#             else:
#                 hmap[s[j]]=1
#             if(j-i+1==len(hmap)):
#                 if(m<j-i+1):
#                     m = j-i+1
#             else:
#                 while(i<j and j-i+1!=len(hmap)):
#                     hmap[s[i]]-=1
#                     if(hmap[s[i]]==0):
#                         del hmap[s[i]]
#                     i+=1
#             j+=1
#         return m