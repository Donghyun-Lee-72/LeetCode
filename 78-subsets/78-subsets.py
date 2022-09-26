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
        elif len(nums_partial) == 0:    # more element to insert; but no numbers left
            return
        
        for i in range(len(nums_partial)):
            next_working = working_list + [nums_partial[i]]
            next_nums_partial = nums_partial[i+1:]
            next_size = size - 1
            if len(next_nums_partial) < next_size:  # reduces time by removing impossible cases
                return
            self.subsets_helper(result, next_working, next_nums_partial, next_size)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        max_size = len(nums)
        for size in range(max_size+1):
            self.subsets_helper(result, [], nums, size)
        return result