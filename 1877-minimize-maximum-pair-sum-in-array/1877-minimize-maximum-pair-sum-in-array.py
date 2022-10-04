class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = [(nums[i],nums[-(i+1)]) for i in range(len(nums)//2)]
        pair_sum = list(map(sum, pairs))
        max_sum = max(pair_sum)
        return max_sum