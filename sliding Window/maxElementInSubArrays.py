from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        i,j = 0,0
        queue = deque([])
        while(j<len(nums)):
            while(queue and nums[queue[-1]]<nums[j]):
                queue.pop()
            queue.append(j)
            if(j-i+1<k):
                j+=1
            else:
                ans.append(nums[queue[0]])
                if(i==queue[0]):
                    queue.popleft()
                i+=1
                j+=1
        return ans
        