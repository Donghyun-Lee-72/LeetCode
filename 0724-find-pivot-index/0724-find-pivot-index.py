class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        allSum = sum(nums)
        leftSum = 0
        curr = None
        
        for i in range(len(nums)):
            curr = nums[i]
            if allSum - curr == leftSum*2:
                return i
            leftSum += curr
        
        return -1