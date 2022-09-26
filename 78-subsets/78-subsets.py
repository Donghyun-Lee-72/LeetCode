class Solution:
    def subsets_helper(self, result:List[int], working_list: List[int], nums_partial: List[int], size) -> None:
        """
        result: List[List[int]]; final result of the mother function
        working_list: List[int]; currently working array
        nums_partial: List[int]; remaining nums available to use
        """
        if size == 0:           # zero size, means we finished working with current length
            result.append(working_list)
            return
        elif len(nums_partial) < size:    # more element to insert; but not enough numbers
            return
        
        for i in range(len(nums_partial)):
            next_working = working_list + [nums_partial[i]]
            self.subsets_helper(result, next_working, nums_partial[i+1:], size - 1)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        max_size = len(nums)
        for size in range(max_size+1):
            self.subsets_helper(result, [], nums, size)
        return result