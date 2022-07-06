class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for char in s:
            if char in ['(', '{', '[']:
                arr.append(char)
            else:
                if len(arr) == 0:
                    return False
                elif arr[-1] == '(' and char == ')':
                    arr = arr[:-1]
                elif arr[-1] == '{' and char == '}':
                    arr = arr[:-1]
                elif arr[-1] == '[' and char == ']':
                    arr = arr[:-1]
                else:
                    return False

        if len(arr) == 0:
            return True
        else:
            return False
                