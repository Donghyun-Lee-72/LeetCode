class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = (len(nums)+1) * (len(nums))/2
        nums_sum = sum(nums)
        missing = int(target - nums_sum)
        return missing