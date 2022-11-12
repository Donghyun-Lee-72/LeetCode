class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        chars = set(list(sentence))
        if len(chars) == 26:
            return True
        else:
            return False
        