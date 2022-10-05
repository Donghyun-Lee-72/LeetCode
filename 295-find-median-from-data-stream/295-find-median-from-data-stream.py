class MedianFinder:
    from bisect import insort
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        insort(self.nums, num)

    def findMedian(self) -> float:
        if len(self.nums) < 1:
            return None
        elif len(self.nums) % 2:
            return self.nums[len(self.nums)//2]
        else:
            return (self.nums[len(self.nums)//2]+self.nums[len(self.nums)//2-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian() 