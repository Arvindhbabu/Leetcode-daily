class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        ind = {x:i+1 for i, x in enumerate(sorted(set(nums)))}
        n, m = len(nums), len(ind)
        Tree_freq = [0] * (m+1)
        Tree_sums = [0] * (m+1)
        def kth(Tree_freq, Tree_sums, k):
            lo = 1
            hi = m
            while lo < hi:
                mid = (lo+hi)//2
                if query(Tree_freq, mid) < k:
                    lo = mid+1
                else:
                    hi = mid
            v = (query(Tree_sums, lo)-query(Tree_sums, lo-1)) // (query(Tree_freq, lo)-query(Tree_freq, lo-1))
            left = query(Tree_freq, lo-1)
            return query(Tree_sums, lo-1) + (k-left) * v + nums[0]
        def update(Tree, i, delta):
            while i < m+1:
                Tree[i] += delta
                i += i & -i
        def query(Tree, i):
            R = 0
            while i > 0:
                R += Tree[i]
                i -= i & -i
            return R
        res = sum(nums[:k+1])
        for i in range(1, n):
            update(Tree_freq, ind[nums[i]], 1)
            update(Tree_sums, ind[nums[i]], nums[i])
            if i > dist:
                score = kth(Tree_freq, Tree_sums, k)
                res = min(res, score)
                update(Tree_freq, ind[nums[i-dist]], -1)
                update(Tree_sums, ind[nums[i-dist]], -nums[i-dist])
        return res

            