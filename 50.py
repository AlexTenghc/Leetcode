"""Implement pow(x, n), which calculates x raised to the power n (i.e., xn)."""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """output = 1

        if n < 0:
            x = (1/x)
            n = abs(n)

        for _ in range(n):
            output = output * x

        return output"""
        """return math.pow(x,n)"""
        return self.exponential(x, n)
            

    def exponential(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            return 1.0 / self.exponential(x, -1 * n)

        if n % 2 != 0:
            return x * self.exponential(x * x, (n-1)//2)
        else:
            return self.exponential(x * x, n//2)
