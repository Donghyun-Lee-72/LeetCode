class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = [0, 0]
        for char in s:
            if char == "(":
                cnt[0] += 1
            else:
                if cnt[0] > 0:
                    cnt[0] -= 1
                else:
                    cnt[1] += 1
        return sum(cnt)