class Solution:
    def helper(self, combinations: List[str], string: str, ongoing_pair: int, remaining_pair: int):
        """
        helper function to generate recursion
        
        combinations: list of all possible combinations, being filleed up
        string: specific string of parentheses currently working on
        ongoing_pair: number of open but unclosed parentheses
        remaining_pair: number of unopened parentheses
        """
        if ongoing_pair == 0 and remaining_pair == 0:
            combinations.append(string)
            return
        
        if ongoing_pair > 0:
            str1 = string + ')'
            self.helper(combinations, str1, ongoing_pair-1, remaining_pair)
        
        if remaining_pair > 0:
            str2 = string + '('
            self.helper(combinations, str2, ongoing_pair+1, remaining_pair-1)
        
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.helper(result, "", 0, n)
        return result