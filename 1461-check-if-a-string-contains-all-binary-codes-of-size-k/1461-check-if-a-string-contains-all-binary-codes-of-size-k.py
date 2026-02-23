class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        total = 1 << k
        seen = [False] * total
        mask = 0
        limit = total - 1

        for i, ch in enumerate(s):
            mask = ((mask << 1) & limit) | int(ch)
            if i >= k-1 and not seen[mask]:
                seen[mask] = True
                total -= 1
                if total == 0:
                    return True
        return False