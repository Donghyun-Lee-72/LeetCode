class StockSpanner:

    def __init__(self):
        import numpy as np
        self.nums = np.array([])

    def next(self, price: int) -> int:
        import numpy as np
        self.nums = np.append(self.nums, int(price))
        # print(self.nums)
        try:
            days = self.nums.shape[0] - np.argwhere(self.nums > price).flatten()[-1] - 1
            # print(np.argwhere(self.nums > price))
            # print("a")
        except:
            days = self.nums.shape[0]
            # print("b")
        # print("*"*10)
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)