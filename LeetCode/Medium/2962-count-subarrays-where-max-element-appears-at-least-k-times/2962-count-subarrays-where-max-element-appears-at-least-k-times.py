class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = 0
        max_idx = [i for i, x in enumerate(nums) if x == max(nums)]

        if len(max_idx) < k:
            return 0
        
        i = 0
        curr_max_cnt = 0
        for j in range(len(nums)):
            if j in max_idx:
                curr_max_cnt += 1
            
            while i <= j and curr_max_cnt >= k:
                if i in max_idx:
                    curr_max_cnt -= 1
                cnt += len(nums) - j
                i += 1
        
        return cnt