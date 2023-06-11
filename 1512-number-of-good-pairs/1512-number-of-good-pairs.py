class Solution:
    def gaussianSum(self, n: int) -> int:
        return n*(n+1) // 2
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        duplicate = set()
        total = 0
        for num in nums:
            if num in duplicate:
                continue
            
            cnt = nums.count(num)
            total += self.gaussianSum(cnt - 1)
            duplicate.add(num)
        
        return total