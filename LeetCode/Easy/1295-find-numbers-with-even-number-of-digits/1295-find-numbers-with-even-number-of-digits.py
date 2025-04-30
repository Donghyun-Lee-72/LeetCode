class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        from math import log10, floor
        return sum([1 for num in nums if floor(log10(num)) % 2])