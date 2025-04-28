class Solution:
    def findMin_helper(self, nums: List[int], mid: int, right: int) -> int:
        if len(nums) < 3:
            return min(nums)
        
        if nums[mid] < nums[right]:
            nums = nums[:mid+1]
            right = mid
            mid = right // 2
            return self.findMin_helper(nums, mid, right)
        else:
            nums = nums[mid:]
            right = len(nums) - 1
            mid = right // 2
            return self.findMin_helper(nums, mid, right)
    
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) - 1
        mid = right // 2
        return self.findMin_helper(nums, mid, right)
    