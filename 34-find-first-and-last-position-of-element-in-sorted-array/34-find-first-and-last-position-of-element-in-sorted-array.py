class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        from bisect import bisect_left, bisect_right
        left = bisect_left(nums, target)
        right = bisect_right(nums, target) - 1
        
        # corner cases
        if len(nums) < 1:
            return [-1,-1]
        elif len(nums) <= left:
            return [-1,-1]
        
        if nums[left] != target:
            return [-1,-1]
        elif nums[right] != target:
            return [-1,-1]
        else:
            return [left,right]