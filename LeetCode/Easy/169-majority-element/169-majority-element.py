class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        key = n // 2
        cnt = dict()
        
        for num in nums:
            new_cnt = cnt.get(num, 0)+1
            cnt[num] = new_cnt
            if key < new_cnt:
                return num
            
        