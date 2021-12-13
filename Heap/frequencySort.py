from heapq import heappush,heappop,heapify
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in nums:
            if(i in hashmap):
                hashmap[i]+=1
            else:
                hashmap[i]=1
        heap = []
        heapify(heap)
        for i in hashmap:
            heappush(heap,(hashmap[i],-i))
        ans = []
        while(heap):
            element = heappop(heap)
            ans += [-element[1]]*element[0]
        return ans