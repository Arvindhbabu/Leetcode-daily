class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        return [f'{h}:{m:02d}' for h in range(12) for m in range(60)
            if (h<<6|m).bit_count()==n]