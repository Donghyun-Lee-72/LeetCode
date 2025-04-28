class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        windows = dict()
        for idx, num in enumerate(nums):
            loc = windows.get(num, [0, [idx, len(nums)-1]])
            loc[0] += 1
            loc[1][1] = idx
            windows[num] = loc
        
        size = 0
        result = 1
        for cnt, window in windows.values():
            length = window[1] - window[0] + 1
            if cnt > size:
                result = length
                size = cnt
            elif cnt == size and result > length:
                result = length
        return result
                