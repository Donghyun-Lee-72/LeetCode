class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return -1*sum([len(str(num)) % 2 - 1 for num in nums])