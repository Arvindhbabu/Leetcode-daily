class SegTree:
    def __init__(self, n):
        self.n = n
        self.mn = [0]*(4*n)
        self.mx = [0]*(4*n)
        self.lazy = [0]*(4*n)

    def push(self, i):
        if self.lazy[i]:
            for c in (2*i, 2*i+1):
                self.mn[c] += self.lazy[i]
                self.mx[c] += self.lazy[i]
                self.lazy[c] += self.lazy[i]
            self.lazy[i] = 0

    def add(self, i, L, R, l, r, v):
        if r < L or R < l:
            return
        if l <= L and R <= r:
            self.mn[i] += v
            self.mx[i] += v
            self.lazy[i] += v
            return
        self.push(i)
        M = (L+R)//2
        self.add(2*i, L, M, l, r, v)
        self.add(2*i+1, M+1, R, l, r, v)
        self.mn[i] = min(self.mn[2*i], self.mn[2*i+1])
        self.mx[i] = max(self.mx[2*i], self.mx[2*i+1])

    def first_zero(self, i, L, R, ql, qr):
        if qr < L or R < ql:
            return -1
        if self.mn[i] > 0 or self.mx[i] < 0:
            return -1
        if L == R:
            return L
        self.push(i)
        M = (L+R)//2
        x = self.first_zero(2*i, L, M, ql, qr)
        if x != -1:
            return x
        return self.first_zero(2*i+1, M+1, R, ql, qr)


class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        st = SegTree(n)
        last = {}
        ans = 0

        for r, x in enumerate(nums):
            p = last.get(x, -1)
            w = 1 if x % 2 == 0 else -1

            st.add(1, 0, n-1, p+1, r, w)

            l = st.first_zero(1, 0, n-1, 0, r)
            if l != -1:
                ans = max(ans, r-l+1)

            last[x] = r

        return ans