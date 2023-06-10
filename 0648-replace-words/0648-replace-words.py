class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        result = ""
        for word in words:
            roots = [ root for root in dictionary if root == word[:len(root)] ]
            
            if roots:
                word = min(roots, key=len)
                
            result += word + " "
        
        return result[:-1]