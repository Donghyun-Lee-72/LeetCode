class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        key_word = strs[0]
        for i in range(len(min(strs, key=len))):
            for j in range(1, len(strs)):
                if strs[j][i] == key_word[i]:
                    pass
                else:
                    return result
            result += key_word[i]
        return result