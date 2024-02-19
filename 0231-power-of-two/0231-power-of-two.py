class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if n > 0 and n.bit_count() == 1 else False