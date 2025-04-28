class Solution:
    from math import prod
    
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        return prod(digits) - sum(digits)