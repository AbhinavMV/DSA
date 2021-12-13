from heapq import heappush,heappop,heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        heapify(heap)
        
        for i in points:
            heappush(heap,(-((i[0]**2)+(i[1]**2)),i))
            if(len(heap)>k):
                heappop(heap)
        ans = []
        while(heap):
            ans.append(heappop(heap)[1])
        return ans