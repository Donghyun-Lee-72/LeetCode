class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff_best = float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            
            while j < k:
                sum_num = nums[i]+nums[j]+nums[k]
                diff = target-sum_num
                diff_best = diff if abs(diff) < abs(diff_best) else diff_best
                
                if diff < 0:
                    k -= 1
                elif diff > 0:
                    j += 1
                else:
                    return target
        
        return target - diff_best