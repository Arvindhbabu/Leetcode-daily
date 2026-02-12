class Solution:
    def longestBalanced(self, s: str) -> int:
        
        s = [ord(ch) - 97 for ch in s]
        n, ans = len(s), 0

        for left in range(n):
            if ans >= n - left: break
            ctr, unique = [0] * 26, 0

            for rght, ch in enumerate(s[left:]):
                unique+= (ctr[ch] == 0)
                ctr[ch]+= 1
                
                if (rght + 1) % unique != 0 or len(set(ctr) - {0}) != 1: continue 
                if rght > ans: ans = rght

        return ans + 1