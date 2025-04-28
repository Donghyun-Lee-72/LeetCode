class Solution:
    def sortSentence(self, s: str) -> str:
        texts = s.split()
        text_orders = { int(text[-1]):text[:-1] for text in texts }
        result_txt = ""
        for i in range(1, len(text_orders)):
            result_txt += text_orders[i] + " "
        
        result_txt += text_orders[len(text_orders)]
        
        return result_txt
        