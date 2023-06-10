class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for jewel in jewels:
            cnt += stones.count(jewel)
        return cnt