class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_dict = {}
        for num in nums:
            if num > 0:
                nums_dict[num] = None
        
        i = 1
        while True:
            if i in nums_dict:
                i += 1
            else:
                return i
            
             