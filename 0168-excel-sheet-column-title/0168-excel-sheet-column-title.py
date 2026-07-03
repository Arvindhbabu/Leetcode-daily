class Solution:
    def convertToTitle(self, n: int) -> str:

        alpha, ans = 'Z'+ ascii_uppercase, ""

        while n:
            n, r = divmod(n,26)
            ans = alpha[r] + ans
            if not r: n-= 1
        return ans