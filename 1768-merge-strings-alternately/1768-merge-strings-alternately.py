class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ""
        for i in range(min(len(word1), len(word2))):
            string += word1[i]
            string += word2[i]
        
        if len(word1) == len(word2):
            pass
        elif len(word1) < len(word2):
            string += word2[len(word1):]
        else:
            string += word1[len(word2):]
        
        return string