class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.ceil(log10(n) / log10(2)) == math.floor(log10(n) / log10(2)) 