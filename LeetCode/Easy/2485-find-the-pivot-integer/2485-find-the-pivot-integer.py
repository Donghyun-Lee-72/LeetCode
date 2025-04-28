class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_one2n = n*(n+1)/2
        cum_sum = 0
        for i in range(1, n+1):
            cum_sum += i
            if cum_sum == sum_one2n - cum_sum + i:
                return i
            elif cum_sum > sum_one2n - cum_sum + i:
                return -1