class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        
        nums_counter = Counter(nums)
        freq_counter = Counter(nums_counter.values())
        max_freq = max(freq_counter.keys())
        return max_freq * freq_counter[max_freq]
        