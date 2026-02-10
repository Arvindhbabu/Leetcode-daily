class Solution:
    def longestBalanced(self, nums):
        ml = 0
        n = len(nums)
        #
        for i in range(n):
            eve = set()
            odd = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    eve.add(nums[j])
                else:
                    odd.add(nums[j])
                if len(eve) == len(odd):
                    ml = max(ml, j - i + 1)
        return ml
