from heapq import heappush,heappop,heapify
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        heapify(heap)
        for i in arr:
            heappush(heap,(-1*abs(i-x),-i))
            if(len(heap)>k):
                heappop(heap)
        ans = []
        for i in heap:
            ans.append(-i[1])
        ans.sort()
        return ans