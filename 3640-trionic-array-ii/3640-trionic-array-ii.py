class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        l = p = q = 0
        n, ans = len(nums), -inf
        tally, prevLeft = nums[0], inf
        for r, (left, rght) in enumerate(pairwise(nums)):    
            if left > rght:
                tally+= rght
                if prevLeft > left: continue
                p = r
                while (l < q) or (l < p - 1 and nums[l] < 0):
                    tally-= nums[l]
                    l+= 1
            elif left < rght:
                tally+= rght
                if prevLeft > left: q = r
                if l < p < q <= r and tally > ans:
                    ans = tally
            elif left == rght:
                tally, l = rght, r + 1 
            prevLeft = left
        return ans
