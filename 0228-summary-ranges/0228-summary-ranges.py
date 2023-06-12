class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [f"{nums[0]}"]
        
        start = nums[0]
        prev = nums[0]
        output = []
        for num in nums[1:]:
            if num == prev + 1:
                prev = num
            elif start == prev:
                string = str(start)
                output.append(string)
                
                start = num
                prev = num
            else:
                string = f"{start}->{prev}"
                output.append(string)
                
                start = num
                prev = num
                
        if start == prev:
            string = str(start)
            output.append(string)
        else:
            string = f"{start}->{prev}"
            output.append(string)
        
        return output