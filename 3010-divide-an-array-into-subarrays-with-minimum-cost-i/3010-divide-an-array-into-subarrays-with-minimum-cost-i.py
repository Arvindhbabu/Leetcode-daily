class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        a = nums[0]
        nums.pop(0)
        nums.sort()
        return a + nums[0] + nums[1]