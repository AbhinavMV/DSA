class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if(nums[i] in seen):
                return [i,seen[nums[i]]]
            else:
                seen[rem] = i
