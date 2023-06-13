class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cutoff = max(candies) - extraCandies
        result = [ True if candy >= cutoff else False for candy in candies]
        return result