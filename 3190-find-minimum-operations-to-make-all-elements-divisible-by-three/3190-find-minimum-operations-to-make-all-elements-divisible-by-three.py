class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            cnt = cnt + 1 if num % 3 else cnt
        
        return cnt