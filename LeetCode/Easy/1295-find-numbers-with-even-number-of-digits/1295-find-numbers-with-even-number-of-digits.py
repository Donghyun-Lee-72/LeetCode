class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        from math import log10, floor

        cnt = 0
        for num in nums:
            cnt += floor(log10(num)) % 2
        return cnt
        