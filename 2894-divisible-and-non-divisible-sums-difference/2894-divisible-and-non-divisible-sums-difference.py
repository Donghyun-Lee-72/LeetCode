class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num = 0
        for i in range(1, n+1):
            num = num + i if i % m else num - i
            
        return num