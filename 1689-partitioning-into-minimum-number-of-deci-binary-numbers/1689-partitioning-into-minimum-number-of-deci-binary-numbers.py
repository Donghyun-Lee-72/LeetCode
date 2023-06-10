class Solution:
    def minPartitions(self, n: str) -> int:
        max_num = 0
        for char in n:
            num = int(char)
            max_num = max(num, max_num)
        return max_num