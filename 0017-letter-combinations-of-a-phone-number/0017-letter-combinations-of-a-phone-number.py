class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def letterCombinations_helper(digits: str, prev_list: List[str]) -> List[str]:
            if len(digits) == 0:
                return prev_list
            
            letters_dict = { '2': "abc",
                            '3': "def",
                            '4': "ghi",
                            '5': "jkl",
                            '6': "mno",
                            '7': "pqrs",
                            '8': "tuv",
                            '9': "wxyz" }
            
            digit = digits[0]
            curr_list = []
            
            if len(prev_list) == 0:
                prev_list = [""]
                
            for prefix in prev_list:
                for letter in letters_dict[digit]:
                    string = prefix + letter
                    curr_list.append(string)
                    
            return letterCombinations_helper(digits[1:], curr_list)
    
        return letterCombinations_helper(digits, [])