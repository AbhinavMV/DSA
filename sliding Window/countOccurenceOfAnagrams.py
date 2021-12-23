class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap = {}
        ans = []
        i,j=0,0
        #count occurence of each letter
        for x in p:
            if(x in hashmap):
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        count = len(hashmap)
        k = len(p)
        while(j<len(s)):
            if(s[j] in hashmap):
                hashmap[s[j]]-=1
                if(hashmap[s[j]]==0):
                    count-=1
            if(j-i+1<k):
                j+=1
            else:
                if(count==0):
                    ans.append(j-k+1)
                if(s[i] in hashmap):
                    if(hashmap[s[i]]==0):
                        count+=1
                    hashmap[s[i]]+=1
                i+=1
                j+=1
        return ans