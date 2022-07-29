class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            table = {}
            isPattern = True
            for char_word, char_pat in zip(word, pattern):
                if char_word == table.get(char_pat):
                    pass
                elif char_pat not in table and char_word not in table.values():
                    table[char_pat] = char_word
                else:
                    isPattern = False
                    break
            if isPattern:
                result.append(word)
        return result