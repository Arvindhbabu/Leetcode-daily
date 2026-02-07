class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        count = 0 
        for c in s:
            if c == 'b':
                count += 1
            elif count > 0:
                res += 1
                count -= 1
                
        return res