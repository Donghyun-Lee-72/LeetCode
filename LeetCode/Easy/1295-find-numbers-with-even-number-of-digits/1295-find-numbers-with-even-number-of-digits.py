class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        from math import log10, floor
        return sum([floor(log10(num)) % 2 for num in nums])