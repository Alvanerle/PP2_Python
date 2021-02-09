#1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum_ = 0
        while n != 0:
            prod *= int(n % 10)
            sum_ += int(n % 10)
            n = int(n / 10)
        return prod - sum_