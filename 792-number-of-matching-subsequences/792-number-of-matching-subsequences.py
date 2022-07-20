class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            last = -1
            for char in word:
                last = s.find(char, last+1)
                if last == -1:
                    break
            if last != -1:
                cnt += 1

        return cnt