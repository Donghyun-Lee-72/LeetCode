class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1 for num in nums if not(len(str(num)) % 2)])