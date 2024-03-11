class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = { char : i for i, char, in enumerate(order) }
        s_sorted = sorted(s, key = lambda char : order_dict[char] if char in order_dict else len(order_dict))
        return "".join(s_sorted)