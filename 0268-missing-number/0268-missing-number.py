class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        target = len(nums)*(len(nums)+1)/2
        return int(target - nums_sum)