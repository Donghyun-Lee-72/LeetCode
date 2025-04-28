class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        cnt = 0
        total = 0
        for j in range(len(nums)):
            total += nums[j]
            while i <= j and not(total * (j-i+1) < k):
                total -= nums[i]
                i += 1
            cnt += j - i + 1
        return cnt