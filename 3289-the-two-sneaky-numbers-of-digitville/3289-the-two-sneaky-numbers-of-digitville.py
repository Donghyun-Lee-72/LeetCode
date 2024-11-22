class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set()
        culprits = []
        for num in nums:
            if num in nums_set: culprits.append(num)
            nums_set.add(num)
        return culprits
            