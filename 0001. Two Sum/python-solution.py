class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        g = dict()
        for i in range(len(nums)):
            g[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            keys = g.keys()
            if (comp in keys) and (g[comp] != i):
                return [i, g[comp]]
